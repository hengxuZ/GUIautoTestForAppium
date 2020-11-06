import requests
from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()

class WithdrawCoin():
    def __init__(self):
        pass
    def get_username_invite(self, inviteCode):
        """
            查询用户名
            :param inviteCode 提币账户
        """
        param = {"inviteCode":inviteCode}
        res = requestUtil.get("/api/users/accountByInviteCode",param)
        return res.json()



if __name__ == '__main__':
    instance = WithdrawCoin()
    print(instance.get_username_invite("OR9CWHZM"))
    pass
