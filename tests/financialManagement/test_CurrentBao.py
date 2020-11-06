import pytest,time
from devApi.financialManagementPage.Impl.CurrentBaoImpl import CurrentBaoImpl
from devApi.propertyPage.Impl.BillImpl import BillImpl

currentBaoImpl = CurrentBaoImpl()
billImpl = BillImpl()

test_transfer_data = [("USDT",100),("ETH",10)]
test_transferOut_data = [("USDT", 100),("ETH",10)]
transferout_bill_data = [("USDT", 100),("ETH",10)]


@pytest.mark.parametrize("coin_type,amount",test_transfer_data)
def test_transfer_in(coin_type,amount):
    ''' 活期宝转入后,校验数量是否正确'''
    print("======测试-活期宝-转入功能======")
    transfer_before_balance = currentBaoImpl.get_one_current_config(coin_type)['balance']
    currentBaoImpl.transfer_in(coin_type,amount)
    time.sleep(1)
    actal_balance = currentBaoImpl.get_one_current_config(coin_type)['balance']
    assert transfer_before_balance - amount == actal_balance


@pytest.mark.parametrize("coin_type,amount", test_transferOut_data)
def test_transferout(coin_type, amount):
    ''' 活期宝转出后,校验数量是否正确'''
    print("======测试-活期宝-转出功能======")
    transfer_before_balance = currentBaoImpl.get_one_current_config(coin_type)['lockAmount']
    currentBaoImpl.transfer_out(coin_type, amount)
    time.sleep(2)
    actal_balance = currentBaoImpl.get_one_current_config(coin_type)['lockAmount']
    assert transfer_before_balance - amount == actal_balance


def test_current_balance():
    '''校验当前用户 净资产估值与锁仓总usdt一致 '''
    print("======测试-活期宝-净资产估值======")
    instance = CurrentBaoImpl()
    current_balance = instance.get_current_balance()
    lockAmounts = instance.get_all_lockAmount_current()
    assert current_balance == lockAmounts



@pytest.mark.parametrize("coin_type,amount", transferout_bill_data)
def test_transferout_bill(coin_type, amount):
    '''检验 转出功能-生成的账单'''
    print("======测试-活期宝-转出|账单======")
    # transfer_before_balance = currentBaoImpl.get_one_current_config(coin_type)['lockAmount']
    # currentBaoImpl.transfer_out(coin_type, amount)
    # time.sleep(2)
    test_transferout(coin_type, amount)
    print("===检验转出|账单===")
    bill_data = billImpl.get_one_bill()
    if bill_data['coinType'] == coin_type and int(bill_data['availableAmountChange']) == amount:
        if float(bill_data['totalAfterChange']) != float(bill_data['frAfterChange']) + float(bill_data['avAfterChange']) : assert False
        print("账单转出数量{num}-校验成功".format(num = amount))
        assert True
    else:
        print("账单转出校验失败")
        assert False

if __name__ == "__main__":
    pytest.main(["-s", "test_CurrentBao.py"])
 