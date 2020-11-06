#coding=UTF-8
from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()

class Bill():
    def __init__(self):
        pass

    def get_bill(self,page,size,walletType,billType,coinType,from_date,to_date):
        '''
        :param page:页数
        :param size: 数据条目
        :param walletType: 钱包类型
        :param billType: 账单类型 如：充值、提现
        :param from_date:查询开始时间-时间戳 单位：日
        :param to_date:查询结束时间-时间戳 单位：日
        :return:返回筛选的账单信息
        '''
        param = {'page':page,'size':size,'walletType':walletType,'billType':billType,'coinType':coinType,'from':from_date,'to':to_date}
        res = requestUtil.get("/api/u/bill/v3",param)
        return res.json()


if __name__ == '__main__':
    instance = Bill()
    pass