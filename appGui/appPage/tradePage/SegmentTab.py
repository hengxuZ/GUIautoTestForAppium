class SegmentTab(object):
    def __init__(self):
        self.headTitle = "交易"
        self.searchBtnXpath = "/rightContainLin']/android.widget.ImageView[@index='0']"
        self.__tabNameList = ["自选","现货","合约","板块"]
        self.__segmentTabXpath = r"/segmentTab']/android.widget.LinearLayout[@index='0']/android.widget.RelativeLayout[@index='placeholder']"

    def get_tabName_xpath(self,tabName):
        '''通过传入名，替换成对应xpath'''
        index = self.__tabNameList.index(tabName)
        return self.__segmentTabXpath.replace('placeholder',str(index))

if __name__ == "__main__":
    instance = SegmentTab()
    # print(instance.get_tabName_xpath('合约'))