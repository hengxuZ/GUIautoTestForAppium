import unittest,time

from appGui.App import App

from appGui.appPage.homePage.MainTradeArea import MainTradeArea

from appGui.common.LocateUtil import LocateUtil

class TestMainTradeArea(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.main_tradeArea = MainTradeArea()

    def test_01_enter_trade_page(self):
        self.locateUtil.click_handle(self.main_tradeArea.btcPair)
        self.assertTrue(self.locateUtil.assert_find_ele(self.main_tradeArea.btcPair), '进入{pair}交易对页面失败'.format(pair=self.main_tradeArea.btcPair))

    @classmethod
    def tearDownClass(self):
        time.sleep(20)
        App.quit()


if __name__ == '__main__':
    unittest.main()
