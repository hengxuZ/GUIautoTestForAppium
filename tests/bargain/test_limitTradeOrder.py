import pytest

from constant.FloatUtil import FloatUtil
from devApi.propertyPage.Impl.PropertyImpl import PropertyImpl
from devApi.bargainPage.Impl.SpotImpl import SpotImpl

spotImpl= SpotImpl()
propertyImpl = PropertyImpl()
floatUtil = FloatUtil()

test_LimitBuy_data = [("ETH_USDT",0.5,200)]
test_LimitSell_data = [("ETH_USDT",0.5,400)]
test_marketBuy_data = [("ETH_USDT",0.5)]
test_marketSell_data = [("ETH_USDT",0.5)]
test_intendSell_data = [("ETH_USDT",0.2,400,420)]
test_intendBuy_data = [("ETH_USDT",0.2,300,280)]
test_cancel_data = [("ETH_USDT",0.5,200)]

##--------基础用例----------##
@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coinType,amount", test_marketBuy_data)
def test_market_buy(coinType,amount):
    print("======测试-交易-市价挂买单======")
    cur_total = propertyImpl.get_wallet_balance(coinType[:-5])['totalAmount']
    spotImpl.market_buy(coinType,amount)
    now_total = propertyImpl.get_wallet_balance(coinType[:-5])['totalAmount']
    assert floatUtil.compare_float(cur_total,now_total-amount,0.01) # 差值在于手续费,后期优化

@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coinType,amount", test_marketSell_data)
def test_market_sell(coinType,amount):
    print("======测试-交易-市价挂卖单======")
    cur_total = propertyImpl.get_wallet_balance(coinType[:-5])['totalAmount']
    spotImpl.market_sell(coinType,amount)
    now_total = propertyImpl.get_wallet_balance(coinType[:-5])['totalAmount']
    assert floatUtil.compare_float(cur_total,now_total-amount,0.01) # 差值在于手续费,后期优化


@pytest.mark.parametrize("coinType,amount,buy_price", test_LimitBuy_data)
def test_limit_buy(coinType,amount,buy_price):
    print("======测试-交易-限价挂买单======")
    coin_froze = propertyImpl.get_wallet_balance("usdt")['coinFroze']
    spotImpl.limit_buy(coinType,amount,buy_price)
    now_froze = propertyImpl.get_wallet_balance("usdt")['coinFroze']
    assert now_froze  == coin_froze + amount * buy_price

@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coinType,amount,sell_price", test_LimitSell_data)
def test_limit_sell(coinType,amount,sell_price):
    print("======测试-交易-限价挂卖单======")
    coin_froze = propertyImpl.get_wallet_balance("usdt")['coinFroze']
    spotImpl.limit_buy(coinType,amount,sell_price)
    now_froze = propertyImpl.get_wallet_balance("usdt")['coinFroze']
    assert now_froze  == coin_froze + amount * sell_price

@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coinType,amount,price,stop_price", test_intendBuy_data)
def test_intend_buy(coinType,amount,price,stop_price):
    print("======测试-交易-计划挂买单======")
    intend_count = spotImpl.find_intend_order_count(coinType)
    spotImpl.intend_buy(coinType,amount,price,stop_price)
    now_intend_count = spotImpl.find_intend_order_count(coinType)
    assert now_intend_count  == intend_count + 1

@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coinType,amount,price,stop_price", test_intendSell_data)
def test_intend_sell(coinType,amount,price,stop_price):
    print("======交易-计划挂卖单======")
    print("==场景：挂单前与挂单后，挂计划单总数一致=====")
    intend_count = spotImpl.find_intend_order_count(coinType)
    spotImpl.intend_sell(coinType,amount,price,stop_price)
    now_intend_count = spotImpl.find_intend_order_count(coinType)
    assert now_intend_count  == intend_count + 1

@pytest.mark.skip(reason='out-of-date api')
@pytest.mark.parametrize("coinType,amount,buy_price", test_cancel_data)
def test_cancel_order(coinType,amount,buy_price):
    print("======测试-交易|撤单======")
    coin_froze = propertyImpl.get_wallet_balance("usdt")['coinFroze']
    id = spotImpl.limit_buy(coinType,amount,buy_price)
    spotImpl.cancel_one_order(id,coinType)
    now_froze = propertyImpl.get_wallet_balance("usdt")['coinFroze']
    assert now_froze  == coin_froze

if __name__ == "__main__":
    pytest.main(["-s", "test_limitTradeOrder.py"])
    pass