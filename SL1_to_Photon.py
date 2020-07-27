import glob
import os
import sys
import zipfile
import tempfile
import argparse
import pyphotonfile
import multiprocessing
from PIL import Image
# from IPython import embed

class SL1Reader:
    def __init__(self, filepath):
        self.zf = zipfile.ZipFile(filepath, 'r')
        self._read_config()
        self.n_layers = 0
        for filename in self.zf.namelist():
            if os.path.dirname(filename) != '':  # skip all files in subdirectorys (e.g. thumbnails)
                continue
            if ".png" in filename:
                self.n_layers += 1

    def _read_config(self):
        try:
            config = self.zf.read('config.ini')
        except KeyError:
            print('ERROR: Did not find %s in zip file' % filename)
        else:
            self.config = {}
            for line in config.decode().splitlines():
                key, value = line.strip().split('=')
                self.config[key.strip()] = value.strip()

    def extract_images(self, dirpath):
        try:
            os.makedirs(dirpath)
        except OSError:
            pass
        for filename in self.zf.namelist():
            if os.path.dirname(filename) != '':  # skip all files in subdirectorys (e.g. thumbnails)
                continue
            if ".png" in filename:
                data = self.zf.read(filename)
                with open(os.path.join(dirpath, filename), 'bw') as f:
                    f.write(data)

if __name__ == '__main__':
    desc = '''Convert an SL1 file to a Photon file.'''
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("sl1_file", help="SL1 file to convert.")
    parser.add_argument("-f", "--force", action='store_true', help="overwrite existing files.")
    # parser.add_argument("--timelapse", action='store_true', default=False, help="set all exposures to 1s. Useful for debugging exposure with no resin.")
    parser.add_argument("-v", "--verbose", action='store_true', default=False)
    parser.add_argument("-o", "--output", help="photon file output path.")
    args = parser.parse_args()
    # print(args)
    if args.output is None:
        base, ext = os.path.splitext(args.sl1_file)
        photon_path = base + '.photon'
    else:
        photon_path = args.output
    if os.path.exists(photon_path) and args.force is False:
        print('ERROR: file {} already exists!. move or use -f flag to force overwrite. Cancelling...'.format(os.path.basename(photon_path)))
        sys.exit(-1)

    sl1 = SL1Reader(args.sl1_file)
    photon = pyphotonfile.Photon()
    photon.exposure_time = float(sl1.config['expTime'])
    photon.exposure_time_bottom = float(sl1.config['expTimeFirst'])
    photon.layer_height = float(sl1.config['layerHeight'])
    photon.bottom_layers = int(sl1.config['numFade'])

    def log(*a, **b):
        if args.verbose:
            print(*a, **b)

    log('=== PARAMETERS ===')
    log('Exposure Time: {}'.format(photon.exposure_time))
    log('Bottom Exposure Time: {}'.format(photon.exposure_time_bottom))
    log('Layer Height: {}'.format(photon.layer_height))
    log('Bottom Layers: {}'.format(photon.bottom_layers))
    log('Layers: {}'.format(sl1.n_layers))
    log('=== CONVERSION ===')

    with tempfile.TemporaryDirectory() as tmpdirname:

        log('extracting layers... ', end='')

        sl1.extract_images(tmpdirname)

        log('DONE')

        layers = sorted(glob.glob(os.path.join(tmpdirname, '*.png')))

        counter = None

        def convert_layer(filepath):
            global counter

            with counter.get_lock():
                counter.value += 1
                log(f"converting layer {counter.value} / {sl1.n_layers}", end='\r')

            Image.open(filepath).rotate(180).save(filepath)
            return photon.create_layer(filepath)

        counter = multiprocessing.Value('i', 0)
        pool = multiprocessing.Pool(initargs=(counter, ))

        photon.layers = pool.map(convert_layer, layers)

        log()


    photon.write(photon_path)
    print('Output file written to: {}'.format(photon_path))

