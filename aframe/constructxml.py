from bs4 import BeautifulSoup as bs
from camerasettings import *
from settings import *
from frameline_a import *

soup = bs("<framelines></framelines>", 'xml')
soup.framelines.append(soup.new_tag("camera"))
fl = soup.framelines
fl.camera.append(soup.new_tag("type"))
fl.camera.append(soup.new_tag("sensor"))
fl.camera.append(soup.new_tag("aspect"))
fl.camera.append(soup.new_tag("hres"))
fl.camera.append(soup.new_tag("vres"))
fl.append(soup.new_tag('surround'))
fl.surround.append(soup.new_tag('opacity'))
fl.surround.opacity.string = '0'

# >>>user framelines>>>

def get_aspect(self):
    wh = str(self.labelActiveSensorArea.text())
    aspect_px_w = wh.split(0)
    aspect_px_h = wh.split(2)
    return round(aspect_px_w / aspect_px_h, 2)






def get_left_right_top_bottom_fla(self):
    asa = str(self.labelActiveSensorArea.text())
    sensor_px_width = asa.split(0)
    sensor_px_height = asa.split(2)
    fla_wh = str(self.labelFLASize.text())
    fla_px_width = fla_wh.split(0)
    fla_px_height = fla_wh.split(2)
    left_line_fla = round((((sensor_px_width - fla_px_width) / 2) + user_offset_x) / sensor_px_width, 5)
    right_line_fla = round((((sensor_px_width - fla_px_width) / 2) + user_offset_x) / sensor_px_width, 5)
    top_line_fla = round((((sensor_px_height - fla_px_height) / 2) + user_offset_y) / sensor_px_height, 5)
    bottom_line_fla = round((((sensor_px_width - fla_px_height) / 2) + user_offset_y) / sensor_px_height, 5)


# <<<user framelines<<<


#----->>>CREATE RECT>>>-----#
def create_rect_xml(self):
    soup.framelines.append(soup.new_tag("rect"))
    fl.rect.append(soup.new_tag("left"))
    fl.rect.append(soup.new_tag("right"))
    fl.rect.append(soup.new_tag("top"))
    fl.rect.append(soup.new_tag("bottom"))
    fl.rect.append(soup.new_tag("border"))
    fl.rect.border.append(soup.new_tag("width"))
    fl.rect.border.append(soup.new_tag("color"))
    fl.rect.append(soup.new_tag("fill"))
    fl.rect.fill.append(soup.new_tag("color"))
    fl.rect.fill.append(soup.new_tag("opacity"))


#----->>>CAMERA>>>-----#
def camera_alexa_classic_xml(self):
    fl.camera.type.string = 'ALEXA Classic'
    fl.camera.sensor.string = "3K"
    s = str(self.comboBoxClassicSensor.currentIndex())
    r = str(self.comboBoxClassicReso.currentIndex())
    if s == '0' and r == '0': # HD
        fl.camera.aspect.string = '1.78'
        fl.camera.hres.string = '2880'
        fl.camera.vres.string = '1620'
    elif s == '0' and r == '1':
        fl.camera.aspect.string = '1.78'
        fl.camera.hres.string = '2868'
        fl.camera.vres.string = '1640'
    else: # 4:3
        fl.camera.aspect.string = '1.33'
        fl.camera.hres.string = '2868'
        fl.camera.vres.string = '2152'
def camera_alexa_xt_xml(self):
    fl.camera.type.string = "ALEXA XT"
    fl.camera.sensor.string = "3K"

def camera_alexa_sxt_xml(self):
    fl.camera.type.string = "ALEXA SXT"
    fl.camera.sensor.string = "3K"

def camera_mini_xml(self):
    fl.camera.type.string = "ALEXA Mini"
    fl.camera.sensor.string = "3K"

def camera_amira_xml(self):
    fl.camera.type.string = "AMIRA"
    fl.camera.sensor.string = "3K"

def camera_mini_lf_xml(self):
    fl.camera.type.string = "ALEXA Mini LF"

def camera_alexa_lf_xml(self):
    fl.camera.type.string = "ALEXA LF"

def camera_alexa_65_xml(self):
    fl.camera.type.string = "ALEXA 65"
#----->>>CODECS>>>-----#

def radio_amira_codec_hd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"
def radio_amira_codec_2k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "1612"

def radio_amira_codec_32k4kuhd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3200"
    fl.camera.vres.string = "1800"

def radio_amira_codec_hds16pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "1600"
    fl.camera.vres.string = "900"

#-----MINI-----#
def radio_mini_codec_hd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"
def radio_mini_codec_2k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "1612"

def radio_mini_codec_28k169(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"
def radio_mini_codec_32k4uhd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3200"
    fl.camera.vres.string = "1800"

def radio_mini_codec_28k43(self):
    fl.camera.aspect.string = "1.33"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "2160"

def radio_mini_codec_2k239ana(self):
    fl.camera.aspect.string = "1.19"
    fl.camera.hres.string = "2560"
    fl.camera.vres.string = "2145"

def radio_mini_codec_hdanapr(self):
    fl.camera.aspect.string = "0.89"
    fl.camera.hres.string = "1920"
    fl.camera.vres.string = "2160"

def radio_mini_codec_34kograw(self):
    fl.camera.sensor.string = "3.4K"
    fl.camera.aspect.string = "1.55"
    fl.camera.hres.string = "3424"
    fl.camera.vres.string = "2202"

def radio_mini_codec_hds16pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "1600"
    fl.camera.vres.string = "900"

#-----SXT-----#
def radio_alexa_sxt_codec_hd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"

def radio_alexa_sxt_codec_2k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"

def radio_alexa_sxt_codec_32k4kuhd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3200"
    fl.camera.vres.string = "1800"

def radio_alexa_sxt_codec_28k169raw(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"

def radio_alexa_sxt_codec_32k169raw(self):
    fl.camera.sensor.string = "3.2K"
    fl.camera.hres.string = "3168"
    fl.camera.vres.string = "1782"

def radio_alexa_sxt_codec_28k43prraw(self):
    fl.camera.aspect.string = "1.33"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "2160"

def radio_alexa_sxt_codec_2k65anapr(self):
    fl.camera.aspect.string = "1.19"
    fl.camera.hres.string = "2560"
    fl.camera.vres.string = "2146"

def radio_alexa_sxt_codec_4kcineanapr(self):
    fl.camera.aspect.string = "1.19"
    fl.camera.hres.string = "2560"
    fl.camera.vres.string = "2146"

def radio_alexa_sxt_codec_26k65anaraw(self):
    fl.camera.aspect.string = "1.19"
    fl.camera.hres.string = "2578"
    fl.camera.vres.string = "2160"

def radio_alexa_sxt_codec_34kograw(self):
    fl.camera.sensor.string = "3.4K"
    fl.camera.aspect.string = "1.55"
    fl.camera.hres.string = "3424"
    fl.camera.vres.string = "2202"

def radio_alexa_sxt_codec_4kcineogpr(self):
    fl.camera.sensor.string = "3.4K"
    fl.camera.aspect.string = "1.55"
    fl.camera.hres.string = "3414"
    fl.camera.vres.string = "2198"

#-----XT-----#
def radio_alexa_xt_codec_hd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"

def radio_alexa_xt_codec_2k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "1612"

def radio_alexa_xt_codec_32k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3200"
    fl.camera.vres.string = "1800"

def radio_alexa_xt_codec_2k43pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "2152"
def radio_alexa_xt_codec_28k43raw(self):
    fl.camera.aspect.string = "1.33"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "2160"
def radio_alexa_xt_codec_6543croppedraw(self):
    fl.camera.aspect.string = "1.19"
    fl.camera.hres.string = "2578"
    fl.camera.vres.string = "2160"
def radio_alexa_xt_codec_34kograw(self):
    fl.camera.sensor.string = "3.4K"
    fl.camera.aspect.string = "1.55"
    fl.camera.hres.string = "4324"
    fl.camera.vres.string = "2202"

#-----ALEXA PLUS-----#
def radio_alexa_plus_codec_hd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"
def radio_alexa_plus_codec_2k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "1612"
#-----ALEXA PLUS 43------#
def radio_alexa_plus_43_codec_hd169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "1620"
def radio_alexa_plus_43_codec_2k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "1612"
def radio_alexa_plus_43_codec_32k169pr(self):
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3200"
    fl.camera.vres.string = "1800"
def radio_alexa_plus_43_codec_2k43pr(self):
    fl.camera.aspect.string = "1.33"
    fl.camera.hres.string = "2868"
    fl.camera.vres.string = "2152"
def radio_alexa_plus_43_codec_28k43raw(self):
    fl.camera.aspect.string = "1.33"
    fl.camera.hres.string = "2880"
    fl.camera.vres.string = "2160"
#-----ALEXA 65-----#
def radio_alexa65_codec_21111og(self):
    fl.camera.sensor.string = "6.5K"
    fl.camera.aspect.string = "2.11"
    fl.camera.hres.string = "6560"
    fl.camera.vres.string = "3100"
def radio_alexa65_codec_1781cropped(self):
    fl.camera.sensor.string = "5K"
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "5120"
    fl.camera.vres.string = "2880"
def radio_alexa65_codec_1501cropped(self):
    fl.camera.sensor.string = "4K"
    fl.camera.aspect.string = "1.50"
    fl.camera.hres.string = "4320"
    fl.camera.vres.string = "2880"
def radio_alexa65_codec_4kuhd(self):
    fl.camera.sensor.string = "4K"
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3840"
    fl.camera.vres.string = "2160"
def radio_alexa65_codec_lfog(self):
    fl.camera.sensor.string = "4K"
    fl.camera.aspect.string = "1.44"
    fl.camera.hres.string = "4448"
    fl.camera.vres.string = "3096"
#-----ALEXA LF-----#
def radio_alexalf_codec_169(self):
    fl.camera.sensor.string = "4K"
    fl.camera.aspect.string = "1.78"
    fl.camera.hres.string = "3840"
    fl.camera.vres.string = "2160"
def radio_alexalf_codec_239(self):
    fl.camera.sensor.string = "4.5K"
    fl.camera.aspect.string = "2.39"
    fl.camera.hres.string = "4448"
    fl.camera.vres.string = "1856"
def radio_alexalf_codec_og(self):
    fl.camera.sensor.string = "4.5K"
    fl.camera.aspect.string = "1.44"
    fl.camera.hres.string = "4448"
    fl.camera.vres.string = "3096"
#-----<<<CODECS<<<-----#
#-----<<<CAMERA<<<-----#

def flines_clicked_check_format_a(self):
    for flinename in fl.find_all('framelineName'):
        if flinename != 'framelineName':
            return flines_clicked_create_format_a(self)
        else:
            fl.framelineName.clear()
            fl.line.clear()
            fl.line.left.clear()
            fl.line.right.clear()
            fl.line.top.clear()
            fl.line.width.clear()
            fl.line.color.clear()

def flines_clicked_create_format_a(self):
    fl.append(soup.new_tag("framelineName", framelineRect="Format_A"))
    update_flinename_format_a(self)
    fl.append(soup.new_tag("line", framelineRect="Format_A"))
    fl.line.append(soup.new_tag("left"))
    fl.line.append(soup.new_tag("right"))
    fl.line.append(soup.new_tag("top"))
    fl.line.append(soup.new_tag("bottom"))
    fl.line.append(soup.new_tag("border"))
    fl.line.append(soup.new_tag("width"))
    fl.line.append(soup.new_tag("color"))


def current_cb_selected(self):
    cb = str(self.comboBoxRatioFLA.currentIndex())

    if cb == '1':
        return "1.3333:1"
    elif cb == '2':
        return "1.66:1"
    elif cb == '3':
        return "1.7777:1"
    elif cb == '4':
        return "1.85:1"
    elif cb == '5':
        return '2.00:1'
    elif cb == '6':
        return "2.39:1"
    elif cb == "Custom":
        pass
    elif cb == '0':
        fl.framelineName.clear()
        fl.line.clear()
        fl.line.left.clear()
        fl.line.right.clear()
        fl.line.top.clear()
        fl.line.width.clear()
        fl.line.color.clear()
    else:
        pass

def update_flinename_format_a(self):
    fl.framelineName.string = current_cb_selected(self) + check_lens_type(self) + check_fline_scale_format_a(self)

def check_lens_type(self):
    active_cam = str(self.stackedWidgetCameraSettings.currentIndex())
    if active_cam == '1': # Alexa Classic
        classicindex = str(self.comboBoxClassicSqueeze.currentIndex())
        if classicindex == '0':
            return ""
        elif classicindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '2': # Xt
        xtindex = str(self.comboBoxXTSqueeze.currentIndex())
        if xtindex == '0':
            return ""
        elif xtindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '3': # SXT
        sxtindex = str(self.comboBoxSXTSqueeze.currentIndex())
        if sxtindex == '0':
            return ""
        elif sxtindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '4': # Mini
        miniindex = str(self.comboBoxMiniSqueeze.currentIndex())
        if xminiindex == '0':
            return ""
        elif miniindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '5': # Amira
        amiraindex = str(self.comboBoxAmiraSqueeze.currentIndex())
        if amiraindex == '0':
            return ""
        elif amiraindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '6': # Mini LF
        minilfindex = str(self.comboBoxMiniLFSqueeze.currentIndex())
        if minilfindex == '0':
            return ""
        elif miniindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '7': # LF
        lfindex = str(self.comboBoxLFSqueeze.currentIndex())
        if lfindex == '0':
            return ""
        elif lfindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'

    elif active_cam == '8': # 65
        sfindex = str(self.comboBox65Squeeze.currentIndex())
        if sfindex == '0':
            return ""
        elif sfindex == '1':
            return "anamorphic1.3x"
        else:
            return 'anamorphic2x'




def check_fline_scale_format_a(self):
    return "_scaling" + str(self.lineEditFlineFormatAPercent.text()) + "%"

def check_fline_color_format_a(self):
    if self.comboBoxFlineFormatAColor == "none":
        fl.line.color.string = "user"
    else:
        fl.line.color.string = self.comboBoxFlineFormatAColor.currentText().lower()

def check_fline_width_format_a(self):
    if int(self.lineEditFlineFormatALine.text()) >= 10:
        fl.line.width.string = "10"
    else:
        fl.line.width.string = self.lineEditFlineFormatALine.text()
#-----FRAMELINES-----#

def cb_flines_format_a_133(self):
    pass

def cb_flines_format_a_166(self):
    pass

def cb_flines_format_a_178(self):
    pass

def cb_flines_format_a_178(self):
    pass

def cb_flines_format_a_239(self):
    pass

def cb_flines_format_b_custom(self):
    pass

def cb_flines_format_b_133(self):
    pass

def cb_flines_format_b_166(self):
    pass

def cb_flines_format_b_178(self):
    pass

def cb_flines_format_b_178(self):
    pass

def cb_flines_format_b_239(self):
    pass

def cb_flines_format_b_custom(self):
    pass

#----->>>CUSTOM ASPECT RATIO A>>>-----#

#-----<<<CUSTOM ASPECT RATIO A<<<-----#

#----->>>CUSTOM ASPECT RATIO B>>>-----#

#-----<<<CUSTOM ASPECT RATIO B<<<-----#

#-----FRAMELINES-----#

#-----<<<SHADING>>>-----#
def shading_format_a_cb_xml(self):
    cba = str(self.comboBoxShadingFormatA.currentText())

    if cba == "25%":
        pass
    elif cba == "50%":
        pass
    elif cba == "75%":
        pass
    elif cba == "100%":
        pass
    else:
        pass

#-----<<<SHADING>>>-----#

def save_xml(self):
    fname = str(self.lineEditFileName.text())
    f = open(fname + ".xml", "w+")
    f.write(soup.prettify())
    f.close()
    #tree.write("102918.xml", pretty_print = True, xml_declaration = True, encoding = 'UTF-8')




#tree = ET.ElementTree(root)



