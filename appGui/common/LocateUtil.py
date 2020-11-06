from selenium.webdriver.support.wait import WebDriverWait
class LocateUtil:
    def __init__(self, driver):
        self.driver = driver

    ### ------------------------- 获取元素节点类  --------------###
    
    def get_ele_by_id(self,id):
        '''
        定位页面Id元素
        :param name:
        :return:
        '''
        try:
            ele_id = "com.bkex.exchangev1:id/%s" % (id)
            ele = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element_by_id(ele_id))
            return ele
        except BaseException:
            print("id找不到当前节点，id为:{element}".format(element=id))

    
    def get_ele_by_text(self,text_content):
        '''
        通过text定位元素
        :param name:
        :return:
        '''
        try:
            path = "//*[@text='%s']" % (text_content)
            ele = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element_by_xpath(path))
            return ele
        except BaseException:
            print("xpath_text找不到当前节点:{element}".format(element=text_content))

    # 
    # def get_ele_by_xpath(self,driver,xpath_content):
    #     '''通过xpath定位元素'''
    #     try:
    #         path = "//[@resource-id='com.bkt.exchange:id/%s" % (xpath_content)
    #         ele = WebDriverWait(driver, 10, 1).until(lambda x: x.find_element_by_xpath(path))
    #         return ele
    #     except BaseException:
    #         print("xpath找不到当前节点:{element}".format(element=xpath_content))

    
    def get_ele_by_accessbility(self,accessbility_content):
        '''通过accessbility定位元素'''
        try:
            path = "//*[@content-desc='%s']" % (accessbility_content)
            return WebDriverWait(self.driver,10,1).until(lambda x: x.find_element_by_xpath(path))
        except BaseException:
            print("accessbility找不到当前节点:{element}".format(element=accessbility_content))

    
    def get_ele_by_deeplyLocate_text(self,element,text_content):
        try:
            path = "//*[@text='%s']" % (text_content)
            return element.find_element_by_xpath(path)
        except BaseException:
            print("deepluyLocate_text找不到当前节点:{element}".format(element=text_content))
    
    def __handle_method(self,name,method):
        '''
        对元素节点获取的方式统一处理
        :param method: 获取节点的方式：id、xpath、text
        :param name: 节点的值
        :return: 返回ele元素节点
        '''
        ele = None
        if method == 'id':
            ele = self.get_ele_by_id(name)
        elif method == 'xpath_text':
            ele = self.get_ele_by_text(name)
        elif method == 'xpath_accessbility':
            ele = self.get_ele_by_accessbility(name)
        return ele

    ### ------------------处理事件类 -------------------  ###
    
    def click_handle(self,name,method='xpath_text'):
        '''通用点击事件'''
        try:
            self.__handle_method(name,method).click()
        except BaseException:
            print("点击事件失败，节点为:{element}".format(element=name))

    
    def input_handle(self,name,value,method='xpath_text'):
        '''通用输入事件
        :name 节点名
        :value 输入值
        '''
        try:
            self.__handle_method(name,method).send_keys(str(value))
        except BaseException:
            print("输入事件失败，节点为:{element}".format(element=name))

    
    def text_handle(self,name,method="xpath_text"):
        '''
        获取节点文本信息
        :param name:
        :return:
        '''
        try:
            return self.__handle_method(name,method).text
        except BaseException:
            print("id为:{element}，获取文本失败".format(element=name))

### --------------------- 断言方法  ---------------- ###
    
    def assert_find_ele(self,name,method="xpath_text"):
        '''
        找当前页面的指定的文本内容
        :param name:
        :return: 查找到了不会出异常，直接输出True
        '''
        try:
            return self.__handle_method(name, method) is not None
        except BaseException:
            print("查找断言失败。节点为:{element}".format(element=name))


### --------------- 手势方法 -------------------   ###
# 滑动方向：面向用户
    def swipe_left(self,x,y,duration=700):
        x1 = x
        x2 = x/5
        y1 = y
        y2 = y

        self.driver.swipe(x1,y1,x2,y2,duration)

    def find_by_scroll(self, item_name):
        '''垂直方向向下滑动滑动，找到文本节点为item_name'''
        item = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "'
            + item_name + '")')
    # # 向右滑动。y轴保持不变，X轴：由小变大
    # def swipe_right(driver,star_x=0.1,stop_x=0.9,duration=2000):
    #     x1 = int(x*star_x)
    #     y1 = int(y*0.5)
    #     x2 = int(x*stop_x)
    #     y2 = int(y*0.5)
    #     driver.swipe(x1,y1,x2,y2,duration)
    #
    # # 向上滑动。x轴保持不变，y轴：由大变小
    # def swipe_up(driver,star_y=0.9,stop_y=0.1,duration=2000):
    #     x1 = int(x*0.5)
    #     y1 = int(y*star_y)
    #     x2 = int(x*0.5)
    #     y2 = int(y*stop_y)
    #     driver.swipe(x1,y1,x2,y2,duration)
    #
    # # 向下滑动。x轴保持不变，y轴：由小变大
    # def swipe_down(driver,star_y=0.1,stop_y=0.9,duration=2000):
    #     x1 = int(x*0.5)
    #     y1 = int(y*star_y)
    #     x2 = int(x*0.5)
    #     y2 = int(y*stop_y)
    #     driver.swipe(x1,y1,x2,y2,duration)
