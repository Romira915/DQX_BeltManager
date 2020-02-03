from PIL import ImageGrab, Image
from pywinauto import Application
from configparser import ConfigParser

def Crop_dqx():
    inifile = ConfigParser()
    inifile.read("systemdata/config.ini", encoding="utf-8")

    app = Application().connect(path=inifile["PATH"]["DQXpath"])
    pil = app['SQEX.CDev.Engine.Framework.MainWindow'].capture_as_image()
    x, y = pil.size

    return pil.crop((x * 0.37013, y * 0.42801, x * 0.71218, y * 0.60311))