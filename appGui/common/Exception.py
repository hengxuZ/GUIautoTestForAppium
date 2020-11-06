from appGui.common.LocateUtil import LocateUtil
class Exception(object):
    def __init__(self):
        self.locate = LocateUtil
        pass

    def alert_handle(self):
        self.locate.click_handle("close","id")