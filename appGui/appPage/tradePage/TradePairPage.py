import os
from constant.JsonUtil import JsonUtil
from appGui.common.LocateUtil import LocateUtil


class TradePairPage:
    def __init__(self):
        self.pair = "ETH/USDT"
        self.buyingBtnId = "btn_buy"
        self.optional = ('加自选','删自选')
        self.currEntrustAssertText = "当前委托"
        self.entrustSucAssertText = "成交均价/委托价"
        self.allCancelBtn = "撤销全部"
        self.cancelAffirmBtn = "确定"
        self.switchEntrustId = "orderType"
        self.marketEntrust = "市价委托"
        self.planEntrust = "计划委托"
        self.priceInputId = "inputEt"
        self.amountInputId = "transaction_quota"
        self.currentPriceId = "current_price"
        self.entrustMarkId = "tradeTypeTv"      # 当前委托 下 订单的标签：如：计划委托
        self.useableId = "useable"              # 可用数
        self.sumbitBtnId = "btn_handle"         # 买入按钮
        self.moneyPasswordId = "moneyPasswordEt"  # 资金密码输入框
        self.noPasswordId = "noPassword"  # 免输入按钮
        self.submitBtnId = "submitBtn" # 资金密码确认框



    def set_price(self,driver):
        self.locateUtil = LocateUtil(driver)
        # 获取当前交易对价格
        current_price = self.locateUtil.text_handle( self.currentPriceId,"id")
        # 低于当前价格的10%挂单
        buying_input_value = round(float(current_price) * (1 - 0.1),2)
        self.locateUtil.input_handle( self.priceInputId, buying_input_value,"id")

    def set_buying_amount(self,driver):
        '''复用-购买数量输入框'''
        self.locateUtil = LocateUtil(driver)
        # 获取当前交易对价格
        current_price = self.locateUtil.text_handle( self.currentPriceId,"id")
        # 按照15U买入
        buying_amount = round(15 / float(current_price),3)
        self.locateUtil.input_handle(self.amountInputId, buying_amount,"id")


    def get_userInfo(self,fileName):
        '''获取用户文本信息'''
        path = self.filePath = os.path.abspath(os.path.join(__file__,"../../../..","userdata/{name}.json".format(name=fileName)))
        return JsonUtil().read_json(path)


if __name__ == "__main__":
    ins = TradePairPage()
    print(ins.get_userInfo("userInfo_alp01"))