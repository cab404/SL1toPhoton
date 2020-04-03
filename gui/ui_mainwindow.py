# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QLocale)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(566, 343)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.Germany))
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout = QVBoxLayout(self.centralWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit_outfile = QLineEdit(self.groupBox)
        self.lineEdit_outfile.setObjectName(u"lineEdit_outfile")

        self.gridLayout_2.addWidget(self.lineEdit_outfile, 1, 1, 1, 1)

        self.lineEdit_infile = QLineEdit(self.groupBox)
        self.lineEdit_infile.setObjectName(u"lineEdit_infile")

        self.gridLayout_2.addWidget(self.lineEdit_infile, 0, 1, 1, 1)

        self.pushButton_open_out = QPushButton(self.groupBox)
        self.pushButton_open_out.setObjectName(u"pushButton_open_out")

        self.gridLayout_2.addWidget(self.pushButton_open_out, 1, 2, 1, 1)

        self.pushButton_open_in = QPushButton(self.groupBox)
        self.pushButton_open_in.setObjectName(u"pushButton_open_in")

        self.gridLayout_2.addWidget(self.pushButton_open_in, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setSpacing(6)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setObjectName(u"formLayout")
        self.exposureLabel = QLabel(self.groupBox_2)
        self.exposureLabel.setObjectName(u"exposureLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.exposureLabel)

        self.exposureBottomLayersLabel = QLabel(self.groupBox_2)
        self.exposureBottomLayersLabel.setObjectName(u"exposureBottomLayersLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.exposureBottomLayersLabel)

        self.exposureBottomLayersSpinBox = QSpinBox(self.groupBox_2)
        self.exposureBottomLayersSpinBox.setObjectName(u"exposureBottomLayersSpinBox")
        self.exposureBottomLayersSpinBox.setMaximum(999)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.exposureBottomLayersSpinBox)

        self.bottomLayersLabel = QLabel(self.groupBox_2)
        self.bottomLayersLabel.setObjectName(u"bottomLayersLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.bottomLayersLabel)

        self.bottomLayersSpinBox = QSpinBox(self.groupBox_2)
        self.bottomLayersSpinBox.setObjectName(u"bottomLayersSpinBox")
        self.bottomLayersSpinBox.setMaximum(999)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.bottomLayersSpinBox)

        self.exposureDoubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.exposureDoubleSpinBox.setObjectName(u"exposureDoubleSpinBox")
        self.exposureDoubleSpinBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStatesVirginIslands))
        self.exposureDoubleSpinBox.setDecimals(1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.exposureDoubleSpinBox)

        self.liftSpeedLabel = QLabel(self.groupBox_2)
        self.liftSpeedLabel.setObjectName(u"liftSpeedLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.liftSpeedLabel)

        self.liftSpeeedSpinBox = QSpinBox(self.groupBox_2)
        self.liftSpeeedSpinBox.setObjectName(u"liftSpeeedSpinBox")
        self.liftSpeeedSpinBox.setMinimum(1)
        self.liftSpeeedSpinBox.setMaximum(999)
        self.liftSpeeedSpinBox.setSingleStep(5)
        self.liftSpeeedSpinBox.setValue(65)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.liftSpeeedSpinBox)

        self.retractSpeedLabel = QLabel(self.groupBox_2)
        self.retractSpeedLabel.setObjectName(u"retractSpeedLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.retractSpeedLabel)

        self.retractSpeeedSpinBox = QSpinBox(self.groupBox_2)
        self.retractSpeeedSpinBox.setObjectName(u"retractSpeeedSpinBox")
        self.retractSpeeedSpinBox.setMinimum(1)
        self.retractSpeeedSpinBox.setMaximum(999)
        self.retractSpeeedSpinBox.setSingleStep(10)
        self.retractSpeeedSpinBox.setValue(150)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.retractSpeeedSpinBox)

        self.layerHeightDoubleSpinBox = QDoubleSpinBox(self.groupBox_2)
        self.layerHeightDoubleSpinBox.setObjectName(u"layerHeightDoubleSpinBox")
        self.layerHeightDoubleSpinBox.setEnabled(False)
        self.layerHeightDoubleSpinBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.layerHeightDoubleSpinBox.setReadOnly(True)
        self.layerHeightDoubleSpinBox.setPrefix(u"")
        self.layerHeightDoubleSpinBox.setDecimals(3)
        self.layerHeightDoubleSpinBox.setSingleStep(0.050000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.layerHeightDoubleSpinBox)

        self.layerHeightLabel = QLabel(self.groupBox_2)
        self.layerHeightLabel.setObjectName(u"layerHeightLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.layerHeightLabel)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_convert = QPushButton(self.centralWidget)
        self.pushButton_convert.setObjectName(u"pushButton_convert")

        self.horizontalLayout.addWidget(self.pushButton_convert)

        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)

        self.horizontalLayout.addWidget(self.progressBar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SL1 to Photon Converter", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"File Selection", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Output File", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input File", None))
        self.lineEdit_outfile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to the Photon-File", None))
        self.lineEdit_infile.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Path to the SL1-File", None))
        self.pushButton_open_out.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.pushButton_open_in.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.exposureLabel.setText(QCoreApplication.translate("MainWindow", u"Exposure", None))
        self.exposureBottomLayersLabel.setText(QCoreApplication.translate("MainWindow", u"Exposure (Bottom Layers)", None))
        self.bottomLayersLabel.setText(QCoreApplication.translate("MainWindow", u"Bottom Layers", None))
        self.liftSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Lifting Speed", None))
        self.retractSpeedLabel.setText(QCoreApplication.translate("MainWindow", u"Retract Speed", None))
        self.layerHeightLabel.setText(QCoreApplication.translate("MainWindow", u"Layer Height", None))
        self.pushButton_convert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

