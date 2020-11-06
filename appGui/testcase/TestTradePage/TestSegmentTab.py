import unittest,time

from appGui.App import App
from appGui.common.LocateUtil import LocateUtil
from appGui.appPage.tradePage.SegmentTab import SegmentTab

class TestSegmentTab(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.segmentTab = SegmentTab()

    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        App.quit()

if __name__ == '__main__':
    unittest.main()
