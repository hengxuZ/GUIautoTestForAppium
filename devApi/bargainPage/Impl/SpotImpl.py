from devApi.bargainPage.Spot import Spot
from devApi.propertyPage.Impl.PropertyImpl import PropertyImpl
propertyImpl = PropertyImpl()

class SpotImpl(Spot):
    def __init__(self):
        pass

    #--限价买单--#
    def limit_buy(self, pair,totalAmount,price):
        res = super().create_trade_limit_order(pair,'BID',"LIMIT",totalAmount,price)
        if res['code'] == 0:
            print("{coin}-挂单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))


    def limit_sell(self,pair,totalAmount,price):
        '''限价卖单'''
        res = super().create_trade_limit_order(pair,'ASK',"LIMIT",totalAmount,price)
        if res['code'] == 0:
            print("{coin}-挂单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))


    def market_buy(self,pair,totalAmount):
        '''市价买单'''
        res = super().create_trade_limit_order(pair,'BID',"MARKET",totalAmount)
        if res['code'] == 0:
            print("{coin}-市价买单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))

    def market_sell(self,pair,totalAmount):
        '''
        市价卖单
        :param pair:交易对
        :param totalAmount:
        :return:
        '''
        res = super().create_trade_limit_order(pair,'BID',"MARKET",totalAmount)
        if res['code'] == 0:
            print("{coin}-市价卖单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))

    def intend_buy(self,pair,totalAmount,price,stopPrice):
        '''计划买单'''
        res = super().create_trade_limit_order(pair, 'BID', "STOP_LIMIT", totalAmount,price,stopPrice)
        if res['code'] == 0:
            print("{coin}-计划委托买单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))


    def intend_sell(self,pair,totalAmount,price,stopPrice):
        '''计划卖单'''
        res = super().create_trade_limit_order(pair, 'ASK', "STOP_LIMIT", totalAmount,price,stopPrice)
        if res['code'] == 0:
            print("{coin}-计划委托卖单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))

    def intend_buy(self,pair,totalAmount,price,stopPrice):
        '''计划买单'''
        res = super().create_trade_limit_order(pair, 'BID', "STOP_LIMIT", totalAmount,price,stopPrice)
        if res['code'] == 0:
            print("{coin}-计划委托买单成功.ID为：{id}".format(coin=pair[0:-5],id=res["data"]))
            return res["data"]
        else:
            print("{res},请求失败".format(res=res))

    def cancel_one_order(self,orderId, pair):
        res = super().cancel_one_order(orderId, pair)
        if res["code"] == 0:
            print("{coin}-撤单成功.".format(coin=pair[0:-5]))
        else:
            print("{res},请求失败".format(res=res))

    def cancel_all_order(self,orderNoPairJson):
        res = super().cancel_all_order(orderNoPairJson)
        if res["code"] == 0:
            print("全部撤单成功.")
        else:
            print("{res},请求失败".format(res=res))

    def get_entrust_order_list(self,pair=''):
        res = super().get_entrust_order_list(pair)
        if res["code"] == 0:
            print("当前委托：如下订单")
            for item in res["data"]["data"]:
                print("币种：{coin}.挂单量：{totalAmount}.挂单价格：{price}.委托类型：{orderType}.委托id为：{id}".format(coin=item["pair"],totalAmount=item["totalAmount"],orderType=item["orderType"],price=item['price'],id=item['id']))
            return res
        else:
            print("{res},请求失败".format(res=res))

    def find_intend_order_count(self,pair):
        '''

        :param pair:
        :return: 计划委托订单数量
        '''
        res = super().get_entrust_order_list(pair)
        if res["code"] == 0:
            print("当前计划委托：如下订单")
            intend_num = 0
            for item in res["data"]["data"]:
                if item["orderType"] == "STOP_LIMIT":
                    intend_num+=1
                    print("找到计划委托单。币种：{coin}.挂单量：{totalAmount}.挂单价格：{price}.委托id为：{id}".format(coin=item["pair"],totalAmount=item["totalAmount"],price=item['price'],id=item['id']))
            return intend_num
        else:
            print("{res},请求失败".format(res=res))

if __name__ == "__main__":
    spotImpl = SpotImpl()
    # propertyImpl.get_wallet_balance("ETH")
    # spotImpl.cancel_one_order(2020092216040008671078660, "ETH_USDT")
    print(spotImpl.intend_buy("ETH_USDT",0.5,400,420))
    # spotImpl.market_buy("ETH_USDT",0.5)
    # spotImpl.cancel_all_order([{"pair":'ETH_USDT',"orderNo":"2020092215565735371043054"},{"pair":'ETH_USDT',"orderNo":"2020092215432453171020337"},{"pair":'ETH_USDT',"orderNo":"2020092215412940771015433"}])
    # propertyImpl.get_wallet_balance("ETH")