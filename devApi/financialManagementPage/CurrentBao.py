from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()

class CurrentBao(object):
    def __init__(self):
        pass
    def all_cointype_config(self):
        """
            获取所有币种对应的个人信息
            :return
                    yearRate币种的七日年化,
                    balance: 当前币种可用数量
                    lockAmount: 锁仓数量
                    price 当前币种价格 0当前没有充值

        """
        res = requestUtil.get("/api/g/current/conf/v2")
        return res.json()

    def current_rank(self):
        """
            data.balance:获取 净资产估值usdt数
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
    def transferin_coin(self,coinType,amount):
        """
           转入货币
           :param coinType 转入的币种
           :param amount 转入数量

           :returns code:0 代表成功 -1 代表失败
        """
        res = requestUtil.post("/api/current/in",{"coinType":coinType,"amount":amount})
        return res.json()

    def transferout_coin(self,coinType, amount):
        """
           转出-活期宝货币
           :param coinType 转出的币种
           :param amount 转出数量

           :returns code:0 代表成功 -1 代表失败
        """
        res = requestUtil.post("/api/current/out",{"coinType":coinType,"amount":amount})
        return res.json()

    def get_only_lock_record(self):
        pass


    def modif_time_yestoday(self):
        sql = """
            
        """
if __name__ == '__main__':
    instance = CurrentBao()
    print(instance.transferin_coin("USDT",100))
    pass