import re,os
from constant.JsonUtil import JsonUtil
from database.initDatabase import InitDatabase
class UserSql():
    def __init__(self):
        pass

    def get_userInfo(self,fileName):
        '''获取用户文本信息'''
        path = self.filePath = os.path.abspath(os.path.join(__file__,"../../..","userdata/{name}.json".format(name=fileName)))
        return JsonUtil().read_json(path)

    def select_userInfo(self,info):
        '''支持通过邮箱、电话找到id'''
        info_str = str(info)
        if info_str.find("@") != -1 :
            type = 'email'
        elif re.search('\d{18,}',info_str):
            type = 'id'
        elif re.search('\d{11}',info_str):
             type = "tel"
        elif re.search('[A-Za-z0-9]{8}',info_str):
            type = "invite_code"
        return type

    def query_user(self,info):
        select_type = self.select_userInfo(info)
        db,cur = InitDatabase().connect_db()
        try:
            sql = """ SELECT id FROM tbl_user WHERE {type} = '{info}'""".format(type=select_type,info=info)
            cur.execute(sql)
            db.commit()
            return cur.fetchone()[0]
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        finally:
            cur.close()

    def recharge_coin(self,userInfo, coinType,amount=10000, walletType='WALLET'):
        '''
        给账户充值钱
        :param userInfo: 账户信息：支持 邮箱、手机号、id的方式
        :param coinType:
        :param walletType:
        :param amount:
        :return:
        '''
        userId = self.query_user(userInfo)
        finalId = "{walType}-{userId}-{coin}".format(walType=walletType, userId=userId, coin=coinType.upper())
        db,cur = InitDatabase().connect_db()
        try:
            sql = """
            INSERT INTO `bkex_exchange`.`tbl_user_ex_account`(`id`, `user_id`, `coin_type`, `coin_amount`, `coin_froze`, `wallet_type`, `update_time`)
            VALUES ('{Id}', '{userId}', '{coinType}', {amount}, 0.000000000000000000, '{walletType}', '2020-10-14 13:29:12')
            ON DUPLICATE KEY UPDATE 
                coin_amount = {amount},
                coin_froze = 0.00000000
            """.format(Id=finalId, userId=userId, coinType = coinType.upper(), walletType=walletType, amount=amount)
            cur.execute(sql)
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        finally:
            print("充值{coin}成功".format(coin=coinType))
            cur.close()


    def go_verified(self,userInfo):
        '''身份认证'''
        select_type = self.select_userInfo(userInfo)
        db, cur = InitDatabase().connect_db()
        try:
            sql = """UPDATE `tbl_user` SET nickname='张富贵',id_no=513002199433939393 WHERE {type} = '{info}'""".format(type=select_type,info=userInfo)
            cur.execute(sql)
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        finally:
            print("身份认证成功")
            cur.close()
    def cancel_verified(self,userInfo):
        '''
        取消-身份认证
        :param userInfo: userInfo: 账户信息：支持 邮箱、手机号、id、UID的方式
        :return:
        '''
        select_type = self.select_userInfo(userInfo)
        db, cur = InitDatabase().connect_db()
        try:
            sql = """UPDATE `tbl_user` SET nickname=NULL ,id_no=NULL 
                WHERE {type} = '{info}'""".format(type=select_type,info=userInfo)
            cur.execute(sql)
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        finally:
            print("删除身份认证成功")
            cur.close()

    def go_google_verified(self,userInfo):
        '''
        绑定谷歌认证
        :param userInfo: userInfo: 账户信息：支持 邮箱、手机号、id、UID的方式
        :return:
        '''
        json_data = self.get_userInfo("userInfo_alp01")

        select_type = self.select_userInfo(userInfo)
        db, cur = InitDatabase().connect_db()
        try:
            sql = """UPDATE `tbl_user` SET google_auth='{secret}',google_status=1 
                WHERE {type} = '{info}'""".format(secret=json_data["googleSecret"],type=select_type,info=userInfo)
            cur.execute(sql)
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        finally:
            print("绑定谷歌认证成功")
            cur.close()

    def cancel_google_verified(self,userInfo):
        '''
        取消绑定谷歌认证
        :param userInfo: userInfo: 账户信息：支持 邮箱、手机号、id、UID的方式
        :return:
        '''
        json_data = self.get_userInfo("userInfo_alp01")

        select_type = self.select_userInfo(userInfo)
        db, cur = InitDatabase().connect_db()
        try:
            sql = """UPDATE `tbl_user` SET google_auth=NULL 
                WHERE {type} = '{info}'""".format(type=select_type,info=userInfo)
            cur.execute(sql)
            db.commit()
        except Exception as e:
            # 如果发生错误则回滚
            db.rollback()
        finally:
            print("取消-绑定谷歌认证成功")
            cur.close()

if __name__ == "__main__":
    ins = UserSql()
    print(ins.recharge_coin("591134058@qq.com","DOT",100))