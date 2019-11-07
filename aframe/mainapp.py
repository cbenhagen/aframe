#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from camerasettings import *


class Aframe(QtWidgets.QMainWindow):
    def __init__(self):
        super(Aframe, self).__init__()
        uic.loadUi('mainapp.ui', self)
        self.setWindowTitle('aframe')
        self.cbCameras.currentIndexChanged.connect(
            lambda: Aframe.default_main_gui(self))
        self.cbSensor.currentIndexChanged.connect(lambda: Cameras.camera_cb_changed(self))
        self.cbReso.currentIndexChanged.connect(lambda: Cameras.reso_cb_changed(self))
        self.cbFormat.currentIndexChanged.connect(lambda: Cameras.formt_cb_changed(self))
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(155, 230, 791, 321))
        self.logo.setPixmap(QtGui.QPixmap("images/aframe_logo.png"))
        self.logo.setObjectName("logo")

    def splash_gui(self):



        return self.logo.show(), self.fCameraSettings.hide(),\
               self.fCenterRatioA.hide(), self.fCenterRatioB.hide(),\
               self.fCenterRatioC.hide(), self.fFrameline.hide(),\
               self.fShading.hide(),self.lFramelineContainer.hide(),\
               self.fRecordingArea.hide(), self.lFLA.hide(), self.lFLB.hide(),\
               self.lFLC.hide(), self.fOffset.hide(), self.fFLStats.hide(),\
               self.fCenterRatioA.hide(), self.fCenterRatioB.hide(),\
               self.fCenterRatioC.hide()

    def default_main_gui(self):
        return self.logo.hide(),\
               self.fCameraSettings.show(), self.fFrameline.show(), self.fShading.hide(),\
               self.lFramelineContainer.show(),self.fRecordingArea.show(),\
               self.lRecordingAreaBG.resize(620, 349),self.lRecordingAreaBG.move(50, 28),\
               self.fOffset.show(),self.fFLStats.show(),self.lFLAText.hide(),\
               self.lFLAScaleText.hide(),self.lFLBText.hide(),self.lFLBScaleText.hide(),\
               self.lFLCText.hide(),self.lFLCScaleText.hide(),self.fCenterRatioA.hide(),\
               self.fCenterRatioB.hide(),self.fCenterRatioC.hide(),Cameras.camera_defaults(self)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Aframe()
    w.show()
    w.splash_gui()
    sys.exit(app.exec_())
