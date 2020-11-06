from devApi.propertyPage.Property import Property

class PropertyImpl(Property):
    def __init__(self):
        pass

    def get_current_price(self,coin):
        res = super().config_price()
        price = float(res['data'][coin]) / float(res['data']['usdt'])
        print('当前{coin}的市价为：{price:.4}'.format(coin=coin,price=price))
        return price

    def get_wallet_balance(self,coinType):
        '''
            格式化钱包余额
            coinType 币种类型
        '''
        res = super().get_wallet_balance()
        for arr in res["data"]["TOTAL"]:
            if arr["coinType"] == coinType.upper():
                print("当前钱包 {coin},可用余额为：{use},冻结额为：{froze}".format(coin=coinType, use=arr['totalAmount']-arr["coinFroze"] ,froze=arr["coinFroze"]))
                return arr
                break

if __name__ == "__main__":
    propertyImpl = PropertyImpl()
    propertyImpl.get_wallet_balance("usdt")