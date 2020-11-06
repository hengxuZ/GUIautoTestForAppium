import unittest,time
from appGui.App import App
from appGui.common.LocateUtil import LocateUtil
from appGui.config.EnvSwitch import EnvSwitch
from appGui.appPage.homePage.TopBar import TopBar
from appGui.appPage.homePage.personalCenterPage.PersonalCenter import PersonalCenter
from appGui.appPage.homePage.personalCenterPage.LoginPage.Login import Login
from appGui.common.AccountInfo import AccountInfo
from script.googleCode import GoogleCodeBuilder

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.login = Login()
        globals()["alreadyLogin"] = False # 是否登录来控制执行不同的用例

    unittest.skipIf(not EnvSwitch().is_online_env(),'测试环境跳过检测弹窗')
    def test_00_has_Toast(self):
        if self.locateUtil.assert_find_ele('close','id'):
            self.locateUtil.click_handle("close", "id")
        else:
            return True

    def test_01_enter_person_page(self):
        '''进入个人页面'''

        if self.locateUtil.assert_find_ele(self.login.leftHeaderId[0],"id"):
            globals()["alreadyLogin"] = False
            self.locateUtil.click_handle(self.login.leftHeaderId[0], "id")
            self.assertTrue(self.locateUtil.assert_find_ele(self.login.title), '进入个人中心页面失败')
        # 已经登录
        elif self.locateUtil.assert_find_ele(self.login.leftHeaderId[1],"id"):
            globals()["alreadyLogin"] = True
            print("用户已经登录")


    def test_02_enter_login_page(self):
        '''进入登录页面'''
        if globals()["alreadyLogin"] == True : return True # 已经登录跳过测试

        self.locateUtil.click_handle(self.login.enterLogin)
        self.assertTrue(self.locateUtil.assert_find_ele( self.login.assertLogin), '进入登录页面失败')


    def test_03_input_phone_with_password(self):
        '''输入邮箱和密码'''
        if globals()["alreadyLogin"] == True: return True  # 已经登录跳过测试

        info = self.login.get_userInfo('userInfo_online') if EnvSwitch().is_online_env() else self.login.get_userInfo('userInfo_sta')

        self.locateUtil.input_handle(self.login.phoneInput,info['account'])
        self.locateUtil.input_handle(self.login.passwordInputId, info['password'],"id")
        self.locateUtil.click_handle(self.login.sumbitLoginId,"id")
        input("滑块验证码操作完毕后请按Enter键")
        # self.assertTrue(self.locateUtil.assert_find_ele(self.login.assertGoogleText),"输入邮箱和密码失败")


    def test_04_input_email_verify(self):
        '''输入验证码,并提交'''
        if globals()["alreadyLogin"] == True: return True  # 已经登录跳过测试
        self.login.select_checkout_method(self.driver)  # 验证码方式
        self.assertTrue(self.locateUtil.assert_find_ele("账号保护"),"登录失败")

    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        App.quit()


if __name__ == '__main__':
    unittest.main()