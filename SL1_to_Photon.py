import glob
import os
import sys
import zipfile
import tempfile
import argparse
import pyphotonfile
import multiprocessing
import io, struct
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
            print('ERROR: Did not find config.ini in zip file. Is that really an SL1 file?')
        else:
            self.config = {}
            for line in config.decode().splitlines():
                key, value = line.strip().split('=')
                self.config[key.strip()] = value.strip()

    def read_thumbnail(self, size="800x480") -> Image:
        try:
            tb = self.zf.read(f'thumbnail/thumbnail{size}.png')
        except KeyError:
            print(f'ERROR: Did not find thumbnail of size {size} in zip file. Is that really an SL1 file?')
        else:
            return Image.open(io.BytesIO(tb))

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
    parser.add_argument("-f", "--force", action='store_true', help="overwrite existing files")
    # parser.add_argument("--timelapse", action='store_true', default=False, help="set all exposures to 1s. Useful for debugging exposure with no resin.")
    parser.add_argument("-v", "--verbose", action='store_true', default=False)
    parser.add_argument("-ls", "--liftspeed", help="lifting speed (65)", default="65")
    parser.add_argument("-rs", "--retractspeed", help="retract speed (150)", default="150")
    parser.add_argument("-o", "--output", help="photon file output path")
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

    photon.version = 2;

    # Printer settings
    photon.bed_x = 68.04000091552734
    photon.bed_y = 120.95999908447266
    photon.bed_z = 155.0

    # Slicing settings
    photon.anti_aliasing_level = 0
    photon.layer_levels = 1
    photon.layer_height = float(sl1.config['layerHeight'])
    photon.bottom_layers = int(sl1.config['numFade'])
    photon.bottom_layer_count = int(sl1.config['numFade'])

    # Lift settings
    photon.lifting_speed = int(args.liftspeed)
    photon.lifting_distance = 5.0

    photon.bottom_lift_speed = int(args.liftspeed)
    photon.bottom_lift_distance = 6.0

    photon.retract_speed = int(args.retractspeed)

    # Curing settings
    photon.exposure_time = float(sl1.config['expTime'])
    photon.exposure_time_bottom = float(sl1.config['expTimeFirst'])
    photon.bottom_light_off_delay = 0.0
    photon.light_off_delay = 0.0
    photon.off_time = 1.0
    photon.light_pwm = 255
    photon.light_pwm_bottom = 255

    # Meta
    photon.volume_ml = float(sl1.config['usedMaterial'])
    photon.weight_g = float(sl1.config['usedMaterial'])
    photon.cost_dollars = 1.0
    photon.print_properties_length = 60
    photon.print_time = int(float(sl1.config['printTime']))
    photon.set_preview_highres(sl1.read_thumbnail(size="800x480"))
    photon.set_preview_lowres(sl1.read_thumbnail(size="400x400"))

    # Strange settings
    photon.p1 = 1.875
    photon.p2 = 9.453131998900351e+23
    photon.p3 = 0.0
    photon.p4 = 8.407790785948902e-45

    def log(*a, **b):
        if args.verbose:
            print(*a, **b)

    log('=== PARAMETERS ===')
    log('Exposure Time: {}'.format(photon.exposure_time))
    log('Bottom Exposure Time: {}'.format(photon.exposure_time_bottom))
    log('Layer Height: {}'.format(photon.layer_height))
    log('Bottom Layers: {}'.format(photon.bottom_layers))
    log('Layers: {}'.format(sl1.n_layers))
    log('Used material: {} g.'.format(sl1.config['usedMaterial']))
    log('Lifting speed: {}'.format(photon.lifting_speed))
    log('Retract speed: {}'.format(photon.retract_speed))
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
