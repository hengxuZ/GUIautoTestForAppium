import unittest,time
from appGui.App import App
from appGui.common.LocateUtil import LocateUtil
from appGui.config.EnvSwitch import EnvSwitch
from appGui.appPage.homePage.personalCenterPage.switchUserPage.SwitchUser import SwitchUser
class TestQuitLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = App.start()
        self.locateUtil = LocateUtil(self.driver)
        self.switchUser = SwitchUser()
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
            # self.locateUtil.click_handle(self.login.leftHeaderId[0], "id")

            self.assertTrue(self.locateUtil.assert_find_ele(self.login.title), '进入个人中心页面失败')
        # 已经登录
        elif self.locateUtil.assert_find_ele(self.login.leftHeaderId[1],"id"):
            globals()["alreadyLogin"] = False
            print("用户已经登录")

    @classmethod
    def tearDownClass(self):
        time.sleep(10)
        App.quit()


if __name__ == '__main__':
    unittest.main()