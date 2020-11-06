from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()

class MiningBao():
    def __init__(self):
        pass
    def mining_cointype_config(self):
        """
            获取所有币种对应的个人信息
            :return
                    yearRate币种的七日年化,
                    balance: 当前币种可用数量
                    lockAmount: 锁仓数量
                    price 当前币种价格 0当前没有充值
        """
        res = requestUtil.get("/api/mining/mining/conf")
        return res.json()

    def current_rank(self):
        """
            data.balance:获取总已存入usdt数
        """
        res = requestUtil.get("/api/g/current/rank/v2")
        return res.json()

    def  current_purchase_history(self):
        """
            data:购买用户的购买量和账户名
        """
        res = requestUtil.get("/api/current/lately")
        return res.json()

### ---------POST----------  ###
    def lock_transferIn_coin(self,coinType,amount):
        """
           转入货币
           :param coinType 转入的币种
           :param amount 转入数量

           :returns code:0 代表成功 -1 代表失败
        """
        res = requestUtil.post("/api/mining/lock/in",{"coinType":coinType,"amount":amount})
        return res.json()

    def lock_transferOut_coin(self,coinType, amount):
        """
           转出-活期宝货币
           :param coinType 转入的币种
           :param amount 转入数量

           :returns code:0 代表成功 -1 代表失败
        """
        res = requestUtil.post("/api/mining/lock/out",{"coinType":coinType,"amount":amount})
        return res.json()

if __name__ == '__main__':
    instance = MiningBao()
    print(instance.lock_transferOut_coin("USDT",100))
    pass