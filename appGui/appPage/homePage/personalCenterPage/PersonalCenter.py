from appGui.appPage.homePage.TopBar import TopBar

class PersonalCenter(TopBar):
    '''个人中心页面'''
    def __init__(self):
        super(PersonalCenter, self).__init__()
        self.title = "个人中心"
        self.enterLogin = "去登录>"
        self.switchUser = "切换账户"
        
        self.verifiyNameId = "rl_real_name"
        self.selectServer = "服务器选择"
        self.useOtherAccountId = "stv_use_other_account"
