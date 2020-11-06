# -*- coding: utf-8 -*
from idlelib import debugger

from behave import *
from devApi.financialManagementPage.CurrentBao import CurrentBao

# 创建实例
instance = CurrentBao()

@step("查询币种{coinType}可用余额")
def step_impl(context,coinType):
    res_json = instance.all_cointype_config()
    for item in res_json['data']['list']:
        if item['coinType'] == coinType:
            context.balance = item['balance']
            break

@step("选择{coinType}转入{amount}")
def step_impl(context, coinType, amount):
    res = instance.transferIn_coin(coinType,amount)
    if res['code'] == 0:
        print("转入成功")
        context.transfer_amount = amount
    else:
        print("转入失败")
        assert False

@step("币种{coinType}可用余额减少{amount}")
def step_impl(context, coinType, amount):
    expect_amount = context.balance - float(context.transfer_amount)
    actal_amount = 0
    res_json = instance.all_cointype_config()
    for item in res_json['data']['list']:
        if item['coinType'] == coinType:
            actal_amount = item['balance']
            break
    assert expect_amount == actal_amount

if __name__ == '__main__':
    pass