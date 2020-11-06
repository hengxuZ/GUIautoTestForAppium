from appGui.appPage.homePage.KingKongDistrictPage.KingKongDistrict import  KingKongDistrict
from constant.JsonUtil import JsonUtil
import os

class RechargeWithdrawal(KingKongDistrict):
    def __init__(self):
        super(RechargeWithdrawal, self).__init__()
        self.selectCoin = "币种选择"
        self.chooseSearchId = "choose_coin_search"
        self.shareQRcodeId = "btnShare"
        self.extractFromChain = "链上提币"
        self.extractFromServer = "站内提币"
        self.withdrawal = "提币"
        self.rechargeText = "充币"
        self.googleNextStep = "下一步"
        self.confirm = "确定"
        self.withdrawalDetail = "提币详情"   # 成功提币确认页面title

        self.fundPasswordId = "password"       # 资金密码id
        self.googlePasswordId = "google_code"  # 谷歌验证码
        self.googleSecretKeyId = 'qrcode_text'
        self.withdrawalAmountId = "amount_et"  # 提币数量
        self.withdrawalAddressId = "address_et" # 提币地址
        self.withdrawalSumbitId = "btnConfirm"  # 提币提交按钮
        self.verifySumbitId = "btn_commit" # 安全认证提交按钮


        # 测试数据
        self.searchData = ("USDT",'TRC20',10) #(搜索币种，最小提币数量)
        self.isChain = False  #控制测试 站内提币or 链上提币 True:代表链上提币 False：站内

    def get_userInfo(self,fileName):
        '''获取用户文本信息'''
        path = self.filePath = os.path.abspath(os.path.join(__file__,"../../../../../..","userdata/{name}.json".format(name=fileName)))
        return JsonUtil().read_json(path)


if __name__ == "__main__":
    l = RechargeWithdrawal()
    print(l.get_userInfo('userInfo_online'))


