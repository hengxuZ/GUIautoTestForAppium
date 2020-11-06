from constant.RequestUtil import RequestUtil
from devApi.financialManagementPage.Impl.CurrentBaoImpl import CurrentBaoImpl

requestUtil = RequestUtil()

class Spot:
    def __init__(self):
        pass

    def get_entrust_order_list(self,pair=''):
        '''获取当前委托所有单(查询对应订单id)
            响应值：委托类型：LIMIT ： 限价委托 STOP_LIMIT:计划委托
        '''
        param = {"pair":pair, "ended":False, "page":1, 'size':20, "asc":False, 'startTime':"", 'endTime':"", 'direction':'','walletType':'','orderType':''}
        res = requestUtil.get("/api/u/trade/orders/list",param)
        return res.json()

    def create_trade_limit_order(self,pair,direction,orderType,totalAmount,price='',stopPrice=''):
        '''
            委托一个订单
            :pair 交易对 如：ETH_USDT
            :direction 方向 BID：Maker ,ASK:Taker
            :orderType 单类型：LIMIT-限价委托 MARKET-市价委托 STOP_LIMIT-计划委托
            :totalAmount 委托量
            :price 挂单价 计划委托模式下 触发价
            :stopPrice 计划委托模式下 成交价(不能为空)
        '''

        operator = 'gte' if orderType == 'STOP_LIMIT' else 'lte'
        payload = {"pair":pair,"direction":direction,"totalAmount":totalAmount,"price":price,"paypassword":'',"walletType":'WALLET',"orderType":orderType,'stopPrice':stopPrice,"operator":operator,"remember":False}

        res = requestUtil.post("/api/u/create_trade_order_newV2",payload)
        return res.json()

    def cancel_one_order(self,orderId, pair):
        '''
        撤单操作
        :param orderId: 委托单id
        :param pair:交易对
        :return:
        '''
        payload = {"orderNo":orderId, "pair":pair, 'paypassword':'','remember':False}
        res = requestUtil.post("/api/u/cancel_trade_order_newV2",payload)
        return res.json()

    def cancel_all_order(self,orderNoPairJson):
        '''
        撤销全部单
        :param orderNoPairJson:列表嵌套字典。如：[{"orderNo":"2020092110064218671070115","pair":"ETH_USDT"},{"orderNo":"2020091914500464771096669","pair":"ETH_USDT"}]
        :return:
        '''
        payload = {"orderNoPairJson":orderNoPairJson,"paypassword":'',"remember":False}
        res = requestUtil.post("/api/u/cancel_trade_orders", payload)
        return res.json()



if __name__ == "__main__":
    spot = Spot()
    print(spot.get_entrust_order_list())
    # print(spot.get_entrust_order_list("ETH_USDT"))

