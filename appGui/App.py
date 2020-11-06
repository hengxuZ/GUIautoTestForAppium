from os.path import abspath,join,dirname
from appium import webdriver

from constant.JsonUtil import JsonUtil
jsonUtil = JsonUtil()

class App:
    driver = ''

    @classmethod
    def start(cls):
        path = abspath(join(dirname(__file__))) + r"\config\device.json"
        device_info = jsonUtil.read_json(path)
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', device_info)
        return cls.driver

    @classmethod
    def quit(cls):
        cls.driver.quit()
