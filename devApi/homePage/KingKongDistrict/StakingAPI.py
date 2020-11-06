from constant.RequestUtil import RequestUtil
requestUtil = RequestUtil()
class Staking:
    def __init__(self):
        pass


    def get_staking_list(self,comingSoon=False,page=1,size=20):
        '''
        :param comingSoon:全部和即将上线的矿池 True：即将上线 False:全部
        :param page:
        :param size:
        :return:
        '''
        param = {"comingSoon":comingSoon,"page":page,"size":size}
        res = requestUtil.get("/api/staking/coin/list",param)
        return res.json()

    def get_staking_coin(self,id):
        '''
        查询单个矿池信息
        :param id:当前矿池对应id
        :return: 当前矿池信息
        '''
        param = {"id":id}
        res = requestUtil.get("/api/staking/coin/info",param)
        return res.json()
# ----------------POST ------------------------ #
    def create_staking_lock(self,stakingCoinId,amount):
        '''
        创建一个锁仓挖矿
        :param stakingCoinId: 锁仓矿池id号
        :param amount: 锁仓数量
        :return:
        '''
        payload = {"stakingCoinId":stakingCoinId,"amount":amount}
        res = requestUtil.post("/api/staking/lock/create",payload)
        return res.json()

    def create_staking_unlock(self, stakingCoinId, amount):
        '''

        :param stakingCoinId: 解锁的矿池ID
        :param amount: 解锁数
        :return:
        '''
        payload = {"stakingCoinId":stakingCoinId,"amount":amount}
        res = requestUtil.post("/api/staking/unlock/create",payload)
        return res.json()

if __name__ == "__main__":
    staking = Staking()
    print(staking.get_staking_list())