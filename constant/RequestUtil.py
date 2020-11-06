from os.path import abspath, join, dirname
import requests
from constant.JsonUtil import JsonUtil
try:
    from urllib import urlencode
# python3
except ImportError:
    from urllib.parse import urlencode

jsonutil = JsonUtil()

URL = "http://bkex.sta"             #STA环境
# URL = "http://bkex.alp"           #ALP环境
# URL = "https://m.djstoken.com"    #线上环境
# URL = "http://bkex.yc"           # 压测环境


class RequestUtil:
    def __init__(self):
        self.baseUrl = URL
        self.token_path = abspath(join(dirname(__file__), "..")) + r"\appGui\config\token.json"

    def get(self,suffix,param={}):
        '''封装符合项目的post请求'''
        url = ''
        if len(param) == 0:
            url = "{baseUrl}{path}".format(baseUrl=self.baseUrl, path=suffix)
        else:
            query = urlencode(param)
            url = "{baseUrl}{path}?{param}".format(baseUrl=self.baseUrl, path=suffix, param=query)

        res = requests.request("GET",url,headers=self._read_header())
        if res.status_code == 403:
            # 再次登录更新Token
            print("403错误,请调用get_login()更新token")
        else:
            return res

    def post(self,suffix,payload={},arg_header={}):
        '''
            封装符合项目的post请求
            :payload 请求体 需要的参数
            :arg_header 请求头
        '''
        self._post_header().update(arg_header)
        url = "{baseUrl}{path}".format(baseUrl=URL,path=suffix)
        res = requests.request("POST", url, headers= self._post_header(),data=payload)
        if res.status_code == 403:
            # 再次登录更新Token
            print("403错误,请调用get_login()更新token")
        else:
            return res

    def _post_header(self):
        '''封装post独有的header'''
        post_header = self._read_header().copy()
        post_header['Content-Type'] = 'application/x-www-form-urlencoded'
        return post_header

    def _read_header(self):
        json_data = jsonutil.read_json(self.token_path)
        return json_data["req_headers"]

if __name__ == "__main__":
    instace = RequestUtil()
    print(instace.get("/api/config/price"))
    pass
