import unittest,time

from appGui.App import App

from appGui.appPage.homePage.KingKongDistrictPage.KingKongDistrict import KingKongDistrict
from appGui.appPage.homePage.KingKongDistrictPage.stakingPage.StakingPage import StakingPage
from appGui.common.LocateUtil import LocateUtil



class TestStaking(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.staking_page = StakingPage()
        self.kingkong = KingKongDistrict()

    def test_00_has_Toast(self):
        if self.locateUtil.assert_find_ele('close','id'):
            self.locateUtil.click_handle("close", "id")
        else:
            return True

    def test_01_enter_staking(self):
        '''进入锁仓挖矿页面'''
        self.locateUtil.click_handle( self.kingkong.staking)
        self.assertTrue(self.locateUtil.assert_find_ele( self.staking_page.title),'进入锁仓挖矿页面失败')

    def test_02_search_coin(self):
        '''搜索币种'''

        self.locateUtil.input_handle(self.staking_page.searchCoin,self.staking_page.searchCoinName)
        self.assertTrue(self.locateUtil.assert_find_ele("{coin}矿池".format(coin=self.staking_page.searchCoinName)),'搜索结果出错')

    def test_03_enter_lock_immediately(self):
        '''进入立即锁仓页面,查找-我的锁仓'''
        self.locateUtil.click_handle( self.staking_page.lockImmediately)
        self.assertTrue(self.locateUtil.assert_find_ele( self.staking_page.myLock), '进入锁仓页面失败')

    def test_04_assert_locked_amount(self):
        '''立即锁仓页面，断言 锁仓数量'''
        locked_amount = "0.1"
        self.locateUtil.input_handle( self.staking_page.lockedAmountInput,locked_amount, 'id')
        self.locateUtil.click_handle(self.staking_page.agreementRadio,"id")  # 点击 我已阅读 点击2次才能生效
        self.locateUtil.click_handle( self.staking_page.agreementRadio, "id")
        self.locateUtil.click_handle( self.staking_page.lockImmediately)
        self.assertEqual(locked_amount,self.locateUtil.text_handle(self.staking_page.sumbitLockedBtn,'id'))

    def test_05_sumbit_locked(self):
        '''检查确认锁仓是否成功'''
        self.locateUtil.click_handle("confirm_btn",'id')
        self.assertTrue(self.locateUtil.assert_find_ele( self.staking_page.lookupOrder), '确认锁仓失败')

    def test_06_enter_order_page(self):
        '''进入锁仓订单页面'''
        self.locateUtil.click_handle( '查看订单')
        self.assertTrue(self.locateUtil.assert_find_ele( self.staking_page.waitForLock), '进入锁仓订单页面失败')

    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        App.quit()

if __name__ == '__main__':
    unittest.main()