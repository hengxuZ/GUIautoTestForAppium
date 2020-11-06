import unittest,time

from appGui.App import App
from appGui.common.AccountInfo import AccountInfo
from appGui.appPage.homePage.KingKongDistrictPage.KingKongDistrict import KingKongDistrict
from appGui.config.EnvSwitch import EnvSwitch
from appGui.appPage.homePage.KingKongDistrictPage.rechargeWithdrawalPage.RechargeWithdrawal import RechargeWithdrawal
from appGui.common.LocateUtil import LocateUtil
from script.googleCode import GoogleCodeBuilder

class TestRechargeWithdrawal(unittest.TestCase):
    '''充提测试'''

    @classmethod
    def setUpClass(self):

        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.recharge = RechargeWithdrawal()

    unittest.skipIf(not EnvSwitch().is_online_env(),'测试环境跳过检测弹窗')
    def test_00_has_Toast(self):
        if self.locateUtil.assert_find_ele('close','id'):
            self.locateUtil.click_handle("close", "id")
        else:
            return True

    def test_01_enter_recharge_page(self):
        '''进入充提币页面'''
        # 找一个金刚区节点，代表加载成功。
        if self.locateUtil.assert_find_ele(self.recharge.staking):
            self.locateUtil.swipe_left(660, 640)  # 滑动金刚区

        self.locateUtil.click_handle(self.recharge.recharge)
        self.assertTrue(self.locateUtil.assert_find_ele(self.recharge.selectCoin),"进入充提页面失败")

    def test_02_search_coin(self):
        '''进入币种充币页面'''
        self.locateUtil.click_handle(self.recharge.searchData[0])
        self.assertTrue(self.locateUtil.assert_find_ele(self.recharge.shareQRcodeId,"id"), "进入充币页面失败")

    def test_03_switch_withdrawal(self):
        '''切换到提币页面'''
        info = self.recharge.get_userInfo('userInfo_alp01') if self.recharge.isChain else self.recharge.get_userInfo('userInfo_alp02')
        self.locateUtil.click_handle(self.recharge.withdrawal)
        if self.recharge.isChain: # 测站内还是链上
            self.locateUtil.input_handle(self.recharge.withdrawalAddressId, info['recharge'][self.recharge.searchData[0]+"_"+self.recharge.searchData[1]], "id")
        else: #站内转
            self.locateUtil.click_handle(self.recharge.extractFromServer)
            self.locateUtil.input_handle(self.recharge.withdrawalAddressId,info['OtherUID'],'id')

        self.locateUtil.input_handle(self.recharge.withdrawalAmountId, self.recharge.searchData[2], "id")
        self.locateUtil.click_handle(self.recharge.withdrawalSumbitId, "id")
        # 账户确认
        self.locateUtil.click_handle(self.recharge.confirm)

        code = GoogleCodeBuilder().get_code(info['googleKey'])

        self.locateUtil.input_handle(self.recharge.fundPasswordId, info["fundPassword"],"id")
        self.locateUtil.input_handle(self.recharge.googlePasswordId,code ,"id")
        self.locateUtil.click_handle(self.recharge.verifySumbitId,"id")

        self.assertTrue(self.locateUtil.assert_find_ele(self.recharge.withdrawalDetail), "提币失败，没有进入提币详情页面")



    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        App.quit()


if __name__ == '__main__':
    unittest.main()
