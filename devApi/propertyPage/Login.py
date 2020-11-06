
from os.path import dirname, join, abspath
from constant.JsonUtil import JsonUtil
from constant.RequestUtil import RequestUtil

requestUtil = RequestUtil()
jsonutil = JsonUtil()

class Login:
    def __init__(self):
        self.token_path = abspath(join(dirname(__file__),"../..")) + r"\appGui\config\token.json"


    def get_login(self,username,password):
        '''登录,并更新Authorization'''
        data = self._get_user_token(username,password)
        res = requestUtil.post("/api/users/token/suffix",{"prefixAuth":data["msg"],"emailCode":123456})
        if res.json()['code'] == 0:
            self._write_token(res.json()['data'])
        else:
            return res.json()

    def _get_user_token(self,username,password):
        '''获取后端返回的登录认证'''
        res = requestUtil.post("/api/users/token",{"username":username,"password":password})
        return res.json()

    def _write_token(self,value):
        '''更新Authorization'''
        junior_json = jsonutil.read_json(self.token_path)
        final_json = junior_json.copy()
        final_json["req_headers"]['Authorization'] = value
        jsonutil.modify_json(self.token_path,final_json)

if __name__ == "__main__":
    login = Login()
    json_data = jsonutil.read_json(login.token_path)
    print(login.get_login(json_data["username"],json_data["password"]))
    pass
