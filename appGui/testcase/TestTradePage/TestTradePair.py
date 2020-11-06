import unittest,time
from appGui.App import App
from appGui.common.LocateUtil import LocateUtil
from appGui.appPage.tradePage.TradePairPage import TradePairPage
from appGui.appPage.BottomNav import BottomNav
class TestTradePair(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.tradePairPage = TradePairPage()
        self.bottomNav = BottomNav()

    def test_01_enter_tradePage(self):
        '''进入交易页面'''
        self.locateUtil.click_handle( self.bottomNav.navNameList[1])
        self.assertTrue(self.locateUtil.assert_find_ele( "最新价"), '进入交易页面失败')

    def test_02_select_nav_inMiddle(self):
        '''选中中间导航栏的usdt'''
        self.locateUtil.click_handle(self.tradePairPage.pair[-4:],"xpath_accessbility")
        self.assertTrue(self.locateUtil.assert_find_ele( "/USDT"), '点击usdt导航失败')

    def test_03_enter_tradePairPage(self):
        '''点击交易对进入交易队页面'''
        self.locateUtil.click_handle( self.tradePairPage.pair)
        self.assertTrue(self.locateUtil.assert_find_ele( self.tradePairPage.buyingBtnId,"id"), '点击交易对进入k线界面失败')

    def test_04_click_buyingBtn(self):
        '''点击买入按钮，进入交易对交易页面'''
        self.locateUtil.click_handle( self.tradePairPage.buyingBtnId,"id")
        self.assertTrue(self.locateUtil.assert_find_ele( self.tradePairPage.currEntrustAssertText), '进入交易对买入界面失败')

    def test_05_buying_limit(self):
        '''限价单挂单'''
        self.tradePairPage.set_price(self.driver)
        self.tradePairPage.set_buying_amount(self.driver)
        self.locateUtil.click_handle( self.tradePairPage.sumbitBtnId, "id")
        # 资金密码
        info = self.tradePairPage.get_userInfo('userInfo_alp01')
        self.locateUtil.input_handle(self.tradePairPage.moneyPasswordId,info["fundPassword"],"id")
        self.locateUtil.click_handle(self.tradePairPage.noPasswordId,"id")
        self.locateUtil.click_handle(self.tradePairPage.submitBtnId,"id")

        self.assertTrue(self.locateUtil.assert_find_ele( self.tradePairPage.entrustSucAssertText), '买入限价单提交失败')

    def test_06_cancal_all(self):
        '''撤销全部挂单'''
        self.locateUtil.click_handle( self.tradePairPage.allCancelBtn)
        self.locateUtil.click_handle(self.tradePairPage.cancelAffirmBtn)
        self.assertFalse(self.locateUtil.assert_find_ele( self.tradePairPage.entrustSucAssertText), '撤销全部-失败')

    def test_07_switch_market_entrust(self):
        '''切换市价委托类型'''
        self.locateUtil.click_handle( self.tradePairPage.switchEntrustId,"id")
        self.locateUtil.click_handle( self.tradePairPage.marketEntrust)
        self.assertTrue(self.locateUtil.assert_find_ele( self.tradePairPage.marketEntrust), '切换委托类型-失败')

    def test_08_buying_market(self):
        '''确认买入市价委托'''
        self.tradePairPage.set_buying_amount(self.driver)
        # 挂单前可用USDT
        pre_amount = self.locateUtil.text_handle(self.tradePairPage.useableId,"id")
        self.locateUtil.click_handle( self.tradePairPage.sumbitBtnId, "id")
        # 挂单后可用USDT
        now_amount = self.locateUtil.text_handle(self.tradePairPage.useableId,"id")
        print("挂单前可用{pre},现在可用{now}".format(pre=pre_amount,now=now_amount))
        self.assertTrue(pre_amount != now_amount, '买入市价单-失败')

    def test_09_switch_plan_entrust(self):
        '''切换plan委托类型'''
        self.locateUtil.click_handle( self.tradePairPage.switchEntrustId,"id")
        self.locateUtil.click_handle( self.tradePairPage.planEntrust)
        self.assertTrue(self.locateUtil.assert_find_ele( self.tradePairPage.planEntrust), '切换委托类型-失败')

    def test_10_buying_plan(self):
        '''计划委托-买入'''
        self.tradePairPage.set_price(self.driver)
        # 写入触发价
        current_price = self.locateUtil.text_handle( self.tradePairPage.currentPriceId,"id")
        self.locateUtil.input_handle("价格",round(float(current_price) * (1 - 0.15),2))

        self.tradePairPage.set_buying_amount(self.driver)
        self.locateUtil.click_handle( self.tradePairPage.sumbitBtnId, "id")
        self.assertTrue(self.locateUtil.assert_find_ele( self.tradePairPage.entrustMarkId,"id"), '买入计划单失败')

    def test_11_cancal_all(self):
        '''撤销全部挂单'''
        self.locateUtil.click_handle( self.tradePairPage.allCancelBtn)
        self.locateUtil.click_handle(self.tradePairPage.cancelAffirmBtn)
        self.assertFalse(self.locateUtil.assert_find_ele( self.tradePairPage.entrustSucAssertText), '撤销全部-失败')

    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        App.quit()


if __name__ == '__main__':
    unittest.main()