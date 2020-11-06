#！/usr/bin/env python
#! -*-coding:utf-8 -*-
#!@Author :RLX
#!@time : 2019/9/26 16:10
import pymysql
import datetime
import random
import os,time
from script import HashEncryption
class Initialization:

    def connect_db(self):
        db = pymysql.connect(user="root", password="bkex.com", host="192.168.3.64",
                                          database="bkex_exchange_ss",
                                          port=3306, charset='utf8mb4')
        cur = db.cursor()
        return db,cur

    def code(self):
        checkcode = ''
        for i in range(6):
            current = random.randrange(0, 4)  # 生成随机数与循环次数比对
            current1 = random.randrange(0, 4)
            if current == i:
                tmp = chr(random.randint(65, 90))  # 65~90为ASCii码表A~Z
            elif current1 == i:
                tmp = chr(random.randint(65, 90))  # 97~122为ASCii码表A~Z
            else:
                tmp = random.randint(0, 9)
            checkcode += str(tmp)
        return checkcode

    def create_info(self,num):
        info = [["{}{}".format((datetime.datetime.now() + datetime.timedelta(minutes=i)).strftime("%Y%m%d%H%M%S%f"),random.randint(10000,99999)),
                 "qaz{}@bkex.co".format(i),
                 i,
                 self.code(),
                 i] for i in range(0,num)]
        if os.path.exists("user_id.txt"):
            os.remove("user_id.txt")
        with open('user_id.txt','a',encoding='utf-8') as f:
            for i in info:
                f.write("{};{};{}\n".format(i[0],i[1],'12345678qa'))
        return info
    def insert_tbl_user(self,info):
        db,cur = self.connect_db()
        now_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for i in info:
            passw=HashEncryption.hashen('12345678qa',i[0])
            print(passw)
            sql = '''INSERT INTO bkex_exchange.tbl_user (id, tel, tel_country_code, email, nickname, country_id, password, 
            vip, pay_password, id_no, last_login_ip, last_login_time, invite_by, invite_code, user_role, google_auth, user_status, 
            wechat_id, update_time, create_time, register_from, real_name, bank_auth_status, id_no_img, user_volunteer_status,slat_status,google_status)
            VALUES ('{id}', null, null, '{email}', null, null, '{password}', 1, NULL , 
            '{id_no}', '172.24.112.140', null, null, '{invite_code}', 'USER', '6dh3 sjxe 3rp2 7xow iacr czgx uxsz knrw', 0, '',
             '{update_time}', '{create_time}', 'email', '{real_name}', '0', null, 0,1,0);'''.format(id=i[0],email=i[1],password=passw,
                                                                                                            id_no=i[2],invite_code=i[3],update_time=now_time,create_time=now_time,
                                                                                                            real_name=i[4])
            cur.execute(sql)
            db.commit()
        cur.close()

    def new_add_money_user(self,info,coinType,avAmount,walletType):
        db, cur = self.connect_db()
        for i in info:
            sql='''INSERT INTO `bkex_exchange`.`tbl_user_ex_account`(`id`, `user_id`, `wallet_type`, `coin_type`, `coin_amount`, `coin_froze`, `update_time`)
             VALUES ('{id}', '{userid}', '{walletType}', '{coinType}', '{avAmount}', 0, '{updata_time}');
'''.format(id=walletType+'-'+i[0]+'-'+coinType,userid=i[0],walletType=walletType,coinType=coinType,avAmount=avAmount,updata_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            cur.execute(sql)
            db.commit()
        cur.close()


    def add_money_trans_account(self,coinType,avAmount,frAmount,walletType):
        #Set_balance(coinType,avAmount,'2019050112000010094000003',frAmount,walletType)
        pass




    def del_purchase_record(self,info):
        db,cur = self.connect_db()
        #sql = '''delete from bkex_exchange.tbl_purchase_order where purchase_id=16'''
        #print(info)
        for i in info:

            sql='''delete from bkex_exchange.tbl_foundation_user_order where foundation_id=28 and user_id="{id}"'''.format(id=i[0])
            #print(sql)
            cur.execute(sql)
            db.commit()
        cur.close()

    def del_user_id(self,info):
        db,cur = self.connect_db()
        for i in info:
            sql = '''delete from bkex_exchange.tbl_user where id="{id}" and email="{email}"'''.format(id=i[0],email=i[1])
            #print(sql)
            cur.execute(sql)
            db.commit()
        cur.close()
    def del_redis(self,info):
        r = self.connect_redis_0()
        for i in info:
           #print(r.get('PURCHASE_SIGN:3:{}'.format(i[0])))
           #r.delete("trans:balance:{}".format(i[0]))

            r.delete("FOUNDATION_ADD_REMARK28_{}".format(i[0]))

    def del_redis_sign_purchase(self,info):
        r = self.connect_redis_0()
        for i in info:

            r.delete('PURCHASE_SIGN:14:{}'.format(i[0]))
            r.delete('PURCHASE_SIGN:16:{}'.format(i[0]))



    def update_purchase_amount(self):
        db,cur = self.connect_db()
        time_point=datetime.datetime.now()
        s_time=time_point.strftime('%Y-%m-%d %H:%M:%S')
        e_time=(time_point+datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
        sql = '''UPDATE `bkex_exchange`.`tbl_purchase` t SET t.now_amount = 0,t.status=0,t.start_time='{}',t.end_time='{}' WHERE t.`id` = 16'''.format(s_time,e_time)
        cur.execute(sql)
        db.commit()
        cur.close()

    def control_add(self,num,coinType,avAmount,walletType):
        info = self.create_info(num)
        self.insert_tbl_user(info)
        #self.add_money_user(info,coinType,avAmount,frAmount,walletType)
        self.new_add_money_user(info,coinType,avAmount,walletType)

    def control_del(self):
        with open('user_id.txt','r',encoding='utf-8') as f:
            info = f.readlines()
            use = []

            for i in info:
                use.append(i.strip("\n").split(";"))
                self.del_user_id(use)
                self.del_redis(use)
                #self.update_purchase_amount()
                self.del_purchase_record(use)
                self.del_redis_sign_purchase(use)
                #self.add_money_trans_account()

if __name__ == '__main__':
    Initialization().control_add(2,'AT',1000,'GENERAL')
    HashEncryption.hashen()