import time, os
from appGui.common.LocateUtil import LocateUtil
from script.googleCode import GoogleCodeBuilder
from constant.JsonUtil import JsonUtil
from appGui.appPage.homePage.personalCenterPage.PersonalCenter import PersonalCenter
from appGui.config.EnvSwitch import EnvSwitch

class Login(PersonalCenter):
    def __init__(self):
        super(Login, self).__init__()  # 继承变量
        self.assertLogin = "登录 BKEX"
        self.phoneInput = "手机号码/邮箱"
        self.passwordInputId = "phone_password"
        self.sumbitLoginId = "btn_login"
        self.assertEmailText = "邮箱验证"
        self.assertGoogleText = "谷歌验证"
        self.getMailCodeId = "get_mail_code"   # 获取邮箱
        self.emailCodeId = "mail_code"
        self.googleCodeId = "google_code"
        self.emailCodeSumbitId = "btn_commit" #邮箱验证码确认


    def select_checkout_method(self,driver):
        '''邮箱和谷歌认证通配'''
        self.locateUtil = LocateUtil(driver)
        # 判断 邮箱还是谷歌
        if self.locateUtil.assert_find_ele(self.assertEmailText):
            self.locateUtil.click_handle(self.getMailCodeId,"id")
            code = input("输入邮箱验证码：")
            self.locateUtil.input_handle(self.emailCodeId, code, "id")
        else:
            # 线上需要等待谷歌验证码，测试环境直接输入已设置好的验证码
            if EnvSwitch().is_online_env():
                code = input("输入谷歌验证码：")
            else:
                code = GoogleCodeBuilder().get_code()
                self.locateUtil.input_handle(self.googleCodeId, code, "id")

        self.locateUtil.click_handle(self.emailCodeSumbitId, "id")
        time.sleep(5) # 网络问题需要等待一定时间

    def get_userInfo(self,fileName):
        '''获取用户文本信息'''
        path = self.filePath = os.path.abspath(os.path.join(__file__,"../../../../../..","userdata/{name}.json".format(name=fileName)))
        return JsonUtil().read_json(path)


if __name__ == "__main__":
    l = Login()
    print(l.get_userInfo('userInfo_online'))
