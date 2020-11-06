from constant.RequestUtil import RequestUtil

class RegularBao():
    def __init__(self):
        self.requestUtil = RequestUtil()

    def pledge_list(self,page=1,size=15):
        """
            :param page 页数
            :param 该页大小

            :return data:募集项目列表 data.totalCount :页面显示项目的个数
        """
        res = self.requestUtil.get("/api/pledge/getList")
        return res


if __name__ == '__main__':
    instance = RegularBao()
    print(instance.pledge_list())