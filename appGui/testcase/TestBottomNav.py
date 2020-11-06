import unittest,time

from appGui.appPage.BottomNav import BottomNav
from appGui.common.LocateUtil import LocateUtil
from appGui.App import App

class TestBottomNav(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.bottomNav = BottomNav()

    def test_01_enter_tradepage(self):
        self.locateUtil.click_handle( self.bottomNav.navNameList[1])
        self.assertTrue(self.locateUtil.assert_find_ele( "最新价"), '进入交易页面失败')
    def test_02_enter_contractpage(self):
        '''进入交易页面'''
        self.locateUtil.get_ele_by_id("ll_tap").find_element_by_xpath("//*[@text='合约']").click()
        self.assertTrue(self.locateUtil.assert_find_ele( "永续合约"), '进入合约页面失败')

    def test_03_enter_financingpage(self):
        '''进入理财页面'''
        self.locateUtil.click_handle(self.bottomNav.navNameList[3])
        self.assertTrue(self.locateUtil.assert_find_ele( "理财资产"), '进入理财页面失败')

    def test_04_enter_propertypage(self):
        '''进入资产页面'''
        self.locateUtil.click_handle(self.bottomNav.navNameList[4])
        self.assertTrue(self.locateUtil.assert_find_ele( "钱包账户"), '进入资产失败')

    def test_05_enter_homepage(self):
        '''进入首页'''
        self.locateUtil.click_handle(self.bottomNav.navNameList[0])
        self.assertTrue(self.locateUtil.assert_find_ele( "币客精选"), '进入首页失败')
    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        App.quit()

if __name__ == '__main__':
    unittest.main()