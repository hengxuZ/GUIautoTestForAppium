import yaml,os
from os.path import abspath
class AccountInfo(object):
    def __init__(self,fileName):
        self.filePath = os.path.abspath(os.path.join(__file__,"../..","userdata/{name}.yaml".format(name=fileName)))
        pass

    def get_user_info(self):
        '''获取用户信息
        :fileName 文件名
        '''
        f = open(self.filePath)
        return yaml.load(f,Loader=yaml.FullLoader)

    def get_user_address(self,typeOfAddress):
        '''
        :param typeOfAddress: 链名称
        :return: 返回 提币地址
        '''
        f = open(self.filePath)
        tmp_json = yaml.load(f,Loader=yaml.FullLoader)
        address = typeOfAddress+"_usdt"
        return tmp_json["recharge"][address]

if __name__ == "__main__":
    acc = AccountInfo("userInfo_online")
    print(acc.get_user_address("TRC20"))