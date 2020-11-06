import requests
from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()

class FinancialManagement():
    def __init__(self):
        pass

    def  financial_property(self):
        """
            data.assetsForUsdt:理财资产数量
        """
        res = requestUtil.get("/api/financialManagement/assets")
        return res

if __name__ == '__main__':
    instance = FinancialManagement()
    print(instance.financial_property())
    pass