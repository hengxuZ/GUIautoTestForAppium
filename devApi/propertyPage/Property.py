import requests
from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()


class Property():
    def __init__(self):
        pass
    def config_price(self):
        """
            获取币种对应usdt和rmb的实时价格
            :return 所有币种对应usdt的价格And人民币的价格
        """
        res = requestUtil.get("/api/config/price")
        return res.json()

    def get_wallet_balance(self):
        """
        :return: 获取个人钱包余额
        """
        res = requestUtil.get("/api/wallet/v2")
        return res.json()


    def get_wallet_single(self,walletType, coinTypes):
        """
        :param walletType:  钱包类型 例如：wallet
        :param coinTypes:   币种类型
        :return: 当前币种的账单
        """
        param = {'walletType':walletType,'coinTypes':coinTypes}
        res = requestUtil.get("/api/wallet/single",param)
        return res.json()

if __name__ == '__main__':
    instance = Property()
    print(instance.get_wallet_single("WALLET","ETH"))
    pass