import pytest, time
from devApi.financialManagementPage.Impl.MiningBaoImpl import MiningBaoImpl

miningBaoImpl = MiningBaoImpl()

test_transferIn_data = [("USDT", 100), ("ETH", 100), ["USDT", 10000]]
test_transferOut_data = [("USDT", 100), ("ETH", 100), ["USDT", 10000]]


@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coin_type,amount", test_transferIn_data)
def test_transfer_in(coin_type, amount):
    ''' 挖矿宝转入后,校验数量是否正确'''
    print("======测试-挖矿宝-转入功能======")

    transfer_before_balance = miningBaoImpl.get_mining_config(coin_type)['balance']
    miningBaoImpl.transfer_in(coin_type, amount)
    time.sleep(1)
    actal_balance = miningBaoImpl.get_mining_config(coin_type)['balance']
    assert transfer_before_balance - amount == actal_balance


@pytest.mark.parametrize("coin_type,amount", test_transferOut_data)
def test_transfer_out(coin_type, amount):
    ''' 挖矿宝转出后,校验数量是否正确'''
    print("======测试-挖矿宝-转出功能======")
    transfer_before_balance = miningBaoImpl.get_mining_config(coin_type)['lockAmount']
    miningBaoImpl.transfer_out(coin_type, amount)
    time.sleep(2)
    actal_balance = miningBaoImpl.get_mining_config(coin_type)['lockAmount']
    assert transfer_before_balance + amount == actal_balance

if __name__ == "__main__":
    pytest.main(["-s", "test_MiningBao.py"])
