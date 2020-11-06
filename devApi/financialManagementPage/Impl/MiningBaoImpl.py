from devApi.financialManagementPage.MiningBao import MiningBao

class MiningBaoImpl(MiningBao):

    def transfer_in(self,coinType, amount):
        '''挖矿宝-转出amount数量'''
        res = super().lock_transferIn_coin(coinType, amount)
        if res['code'] == 0:
            print("转入{type} {num} 枚成功".format(type=coinType, num=amount))
            return True
        else:
            print("转入失败")
            return False

    def transfer_out(self,coinType, amount):
        '''挖矿宝-转出amount数量'''
        res = super().lock_transferIn_coin(coinType, amount)
        if res['code'] == 0:
            print("转出{type} {num} 枚成功".format(type=coinType, num=amount))
            return True
        else:
            print("转出失败")
            return False

    def get_mining_config(self,coinType):
        '''获取当前coinType可用数量'''
        res_json = super().mining_cointype_config()
        for item in res_json['data']['list']:
            if item['coinType'] == coinType:
                print("币种{coin},可用余额{balance},冻结额{lock}".format(coin=coinType, balance=item['balance'],lock=item['lockAmount']))
                return item

    def get_all_lockAmount_mining(self):
        '''获取锁仓币种usdt之和'''
        res_json = super().mining_cointype_config()
        total_usdt = 0
        for item in res_json['data']['list']:
            if item['lockAmount'] != 0:
                total_usdt = item['lockAmount'] * item['price'] + total_usdt

        return total_usdt

    def get_mining_totalLockAmount(self):
        '''获取 净资产估值usdt数'''
        res_json = super().mining_cointype_config()
        if res_json["code"] == 0:
            return res_json['data']['totalLockAmount']
        else:
            print('接口响应失败,实际内容为：{data}'.format(data=res_json))


if __name__ == "__main__":
    instance = MiningBaoImpl()
    print(instance.get_balance('USDT'))
    pass