from devApi.financialManagementPage.CurrentBao import CurrentBao


class CurrentBaoImpl(CurrentBao):

    def transfer_in(self,coinType, amount):
        '''活期宝转入amount数量'''
        res = super().transferin_coin(coinType, amount)
        if res['code'] == 0:
            print("转入{type} {num} 枚成功".format(type=coinType, num=amount))
            return True
        else:
            print("{res},请求失败".format(res=res))
            return False

    def transfer_out(self,coinType, amount):
        '''活期宝-转出amount数量'''
        res = super().transferout_coin(coinType, amount)
        if res['code'] == 0:
            print("转出{type} {num} 枚成功".format(type=coinType, num=amount))
            return True
        else:
            print("{res},请求失败".format(res=res))
            return False

    def get_one_current_config(self,coinType):
        '''获取当前coinType的数据'''
        res_json = super().all_cointype_config()
        for item in res_json['data']['list']:
            if item['coinType'] == coinType.upper():
                print("币种{coin},可用余额{balance},冻结额{lock}".format(coin=coinType,balance=item['balance'],lock=item['lockAmount']))
                return item

    def get_all_lockAmount_current(self):
        '''获取锁仓币种usdt之和'''
        res_json = super().all_cointype_config()
        total_usdt = 0
        for item in res_json['data']['list']:
            if item['lockAmount'] != 0:
                total_usdt = item['lockAmount'] * item['price'] + total_usdt
        return total_usdt

    def get_current_balance(self):
        '''获取 净资产估值usdt数'''
        res_json = super().current_rank()
        if res_json["code"] == 0:
            return res_json['data']['balance']
        else:
            print('接口响应失败,实际内容为：{data}'.format(data=res_json))

if __name__ == "__main__":
    instance = CurrentBaoImpl()
    # print(instance.get_all_lockAmount_current())
    print(instance.get_one_current_config("ETH"))
    pass