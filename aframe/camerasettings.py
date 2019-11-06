from aframe import *
from cameraspecs import *


class Cameras(Aframe):
    def __init__(self, sensor='',reso='',formt='',sen_w=''
                 ,sen_h='',rec_w='',rec_h=''
):
        super().__init__()
        self.sensor = sensor
        self.reso   = reso
        self.formt  = formt
        self.sen_w  = sen_w
        self.sen_h  = sen_h
        self.rec_w  = rec_w
        self.rec_h  = rec_h

    def formt_cb_changed(self):
        _cam = self.cbCameras.currentText()
        _fmt = self.cbFormat.currentText()

        if _cam == 'Alexa Mini' or _cam == 'Amira' or _cam == 'Alexa Mini LF':
            if _fmt == "Apple ProRes":
                block_sigs(self)
                self.cbReso.addItems(cam_settngs[f'{_cam} Apple ProRes'])
                unblock_sigs(self)
                print('formt changed ProRes')

            else:
                block_sigs(self)
                self.cbReso.addItems(cam_settngs[f'{_cam} ARRIRAW'])
                unblock_sigs(self)
                Print('formt changed raw')

        elif _cam in ('Alexa Classic', 'Alexa XT', 'Alexa SXT', 'Alexa LF', 'Alexa 65'):

            print('conditional worked')

    def camera_cb_changed(self):
        cam = self.cbCameras.currentText()
        self.sensor = self.cbSensor.currentText()
        self.reso = self.cbReso.currentText()
        self.formt = self.cbFormat.currentText()
        no_sensor_settng = f'{cam} {self.reso} {self.formt}'
        has_sensor_settng = f'{cam} {self.sensor} {self.reso} {self.formt}'
        self.lCamera.setText(cam)

        if cam == 'Alexa Mini' or cam == 'Amira' or cam == 'Alexa Mini LF':
            if no_sensor_settng in cam_settngs:
                self.sen_w = cam_settngs[no_sensor_settng][0][0]
                self.sen_h = cam_settngs[no_sensor_settng][0][1]
                self.rec_w = cam_settngs[no_sensor_settng][0][2]
                self.rec_h = cam_settngs[no_sensor_settng][0][3]
                self.lActiveSensorArea.setText(f'{self.rec_w} x {self.rec_h} px')
                self.lRecordingArea.setText(f'{self.rec_w} x {self.rec_h} px')
                calc_mm(self)
                print(cam_settngs[no_sensor_settng])

            else:
                if self.formt == "Apple ProRes":
                    block_sigs(self)
                    self.cbReso.addItems(cam_settngs[f'{cam} {self.formt}'])
                    unblock_sigs(self)
                print('camera selected,  Mini Amira or Mini LF didnt work')

        elif cam == 'Alexa Classic' or cam == 'Alexa XT' or cam == 'Alexa SXT' or cam == 'Alexa LF' or cam == 'Alexa 65':
            if has_sensor_settng in cam_settngs:
                self.sen_w = cam_settngs[has_sensor_settng][0][0]
                self.sen_h = cam_settngs[has_sensor_settng][0][1]
                self.rec_w = cam_settngs[has_sensor_settng][0][2]
                self.rec_h = cam_settngs[has_sensor_settng][0][3]
                self.lActiveSensorArea.setText(f'{self.rec_w} x {self.rec_h} px')
                self.lRecordingArea.setText(f'{self.rec_w} x {self.rec_h} px')
                calc_mm(self)
                print(cam_settngs[has_sensor_settng], ' worked')

            else:
                print('camera selected, Classic, XT, SXT, LF, or 65 didnt work')

    def camera_defaults(self):
        cam_sel  = Cameras.camera_cb_changed(self)
        block = Cameras.block_sigs(self)
        unblock = Cameras.unblock_sigs(self)
        cam = self.cbCameras.currentText()
        self.cbSensor.show()
        self.lSensor.show()
        self.cbFormat.move(180, 40)
        self.lFormat.move(180, 10)
        print('cam settings default')

        if cam == 'Alexa Classic':
            print('cam settings defaults: classic')
            return block, self.cbSensor.addItems(cam_settngs['Alexa Classic sensor']), \
                   self.cbReso.addItems(cam_settngs['Alexa Classic 16:9 HD Apple ProRes'][1]), \
                   self.cbFormat.addItem('Apple ProRes'),unblock, cam_sel


        elif cam == 'Alexa XT':
            block
            self.cbSensor.addItems(cam_settngs['Alexa XT sensor'])
            self.cbReso.addItems(cam_settngs['Alexa XT 16:9 HD Apple ProRes'][1])
            self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
            unblock, cam_sel
            print('XT')

        elif cam == 'Alexa SXT':
            block_sigs()
            self.cbSensor.addItems(cam_settngs['Alexa SXT sensor'])
            self.cbReso.addItems(cam_settngs['Alexa SXT 16:9 2.8K ARRIRAW'][1])
            self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
            self.cbFormat.setCurrentText('ARRIRAW')
            unblock_sigs()
            cam_sel.camera_cb_changed()
            print('SXT')

        elif cam == 'Alexa LF':
            block_sigs(self)
            self.cbSensor.addItems(cam_settngs['Alexa LF sensor'])
            self.cbSensor.setCurrentText(cam_settngs['Alexa LF sensor'][0][0])
            self.cbReso.addItem('4K UHD')
            self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
            self.cbFormat.setCurrentText('ARRIRAW')
            cam_sel.unblock_sigs()
            cam_sel.camera_cb_changed()
            print('LF')

        elif cam == 'Alexa 65':
            cam_sel.block_sigs()
            self.cbSensor.addItems(cam_settngs['Alexa 65 sensor'])
            self.cbSensor.setCurrentText('LF 16:9')
            self.cbReso.addItem(cam_settngs['Alexa 65 Open Gate 6560 x 3100 ARRIRAW'][1][0])
            self.cbFormat.addItem('ARRIRAW')
            cam_sel.unblock_sigs()
            cam_sel.camera_cb_changed()
            print('65 ', cam_settngs['Alexa 65 Open Gate 6560 x 3100 ARRIRAW'][1][0])

        else:
            pass

        if cam == 'Alexa Mini' or cam == 'Amira' or cam == 'Alexa Mini LF':
            self.cbSensor.hide()
            self.lSensor.hide()
            self.cbFormat.move(0, 40)
            self.lFormat.move(0, 10)

            if cam == 'Alexa Mini':
                cam_sel.block_sigs()
                self.cbReso.addItems(cam_settngs['Alexa Mini Apple ProRes'])
                self.cbReso.setCurrentText('HD')
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                cam_sel.unblock_sigs()
                cam_sel.camera_cb_changed()
                print('Mini')

            elif cam == 'Amira':
                cam_sel.block_sigs()
                self.cbReso.addItems(cam_settngs['Amira Apple ProRes'])
                self.cbReso.setCurrentText('HD')
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                cam_sel.unblock_sigs()
                cam_sel.camera_selected()
                print('Amira')

            elif cam == 'Alexa Mini LF':
                cam_sel.block_sigs()
                self.cbReso.addItems(cam_settngs['Alexa Mini LF ARRIRAW'])
                self.cbFormat.addItems(['Apple ProRes', 'ARRIRAW'])
                self.cbFormat.setCurrentText('ARRIRAW')
                cam_sel.unblock_sigs()
                cam_sel.camera_cb_changed()
                print('Mini LF')

            else:
                pass

    def block_sigs(self):
        self.cbSensor.blockSignals(True)
        self.cbReso.blockSignals(True)
        self.cbFormat.blockSignals(True)
        self.cbSensor.clear()
        self.cbReso.clear()
        self.cbFormat.clear()

    def unblock_sigs(self: object) -> object:
        self.cbSensor.blockSignals(False)
        self.cbReso.blockSignals(False)
        self.cbFormat.blockSignals(False)


def calc_mm(self):
    print('calc mm')
    mm = 0.00825
    mm_w = round((int(self.rec_w) * mm), 2)
    mm_h = round((int(self.rec_h) * mm), 2)
    self.lActiveSensorMM.setText(f'{str(mm_w)} x {str(mm_h)} mm')
