from devApi.propertyPage.Bill import Bill
import datetime,time


class BillImpl(Bill):

    def get_one_bill(self):
        '''
            挖矿、活期-转入、转出一条数据校验
            :return 返回 账单 最新一条账单信息
        '''
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        # 明天开始时间戳
        tomorrow_start_time = int(time.mktime(time.strptime(str(tomorrow), '%Y-%m-%d')) * 1000)
        res = super().get_bill(1,1,'WALLET','','',0,tomorrow_start_time)
        if len(res['data']['data']) != 0:
            print("当前账单-最新的记录{record}".format(record=res['data']['data']))
            return res['data']['data'][0]
        else :
            print("当前账单-没有满足要求的数据")

if __name__ == '__main__':
    instance = BillImpl()
    print(instance.get_one_bill())
    pass