from bs4 import BeautifulSoup as bs
from camerasettings import Cameras

def xml_init(self):
    soup = bs('<framelines></framelines>', 'xml')
    soup.framelines.append(soup.new_tag('camera'))
    fl = soup.framelines
    fl.camera.append(soup.new_tag('type'))
    fl.camera.append(soup.new_tag('sensor'))
    fl.camera.append(soup.new_tag('aspect'))
    fl.camera.append(soup.new_tag('hres'))
    fl.camera.append(soup.new_tag('vres'))

    fl.append(soup.new_tag('surround'))


class AddComments(Cameras):
    def __init__(self):
        super().__init__()

    def xcam_selected(self, current_cam=self.cbCameras.currentText()):
        cam_mu  = bs(f"<b><!--Frameline definition for {current_cam}--></b>")
        cam_cmt = soup.b.string
        type(cam_cmt)

        sh_a_mu = bs(f"<!-- Shading Format A -->")
        sh_a_cmt = soup.b.string

        sh_bx_upr_mu = f"<!-- Shading Box Upper -->"
        sh_bx_upr_cmt = soup.b.string

    def xml_comments(self):
        pass
        # ADD THESE LINES FOR XML COMMENTS
        # f"<!-- Shading Box {} -->"
        # f"<!-- {} line -->"
        # f"<!-- Format {} {}"
        # f"<!-- {} {} {} line -->"

if __name__ == '__main__':
    xml_init()

