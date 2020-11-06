from devApi.homePage.KingKongDistrict.StakingAPI import Staking



class StakingImpl(Staking):
    def __init__(self):
        pass

    def get_staking_coin(self,id):
        '''查询当前锁仓列表有无某id的矿池'''
        res = super().get_staking_coin(id)
        if res['code'] == 0:
            print("查询矿池为{coinType}".format(coinType=res["data"]["coinType"]))
        return res

    def create_staking_lock(self,id,amount):
        res = super().create_staking_lock(id,amount)
        if res['code'] == 0:
            print("锁仓成功")
            return res
        else:
            print("{res},请求失败".format(res=res))


if __name__ == "__main__":
    staking = StakingImpl()
    print(staking.get_staking_coin())
    pass