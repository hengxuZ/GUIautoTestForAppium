import pymysql

class InitDatabase(object):
    def __init__(self):
        # self.data_url = '192.168.3.64' # sta环境
        self.data_url = '192.168.3.42' # ide环境
        # self.database = "bkex_exchange_ss"
        self.database = "bkex_exchange"
    def connect_db(self):
        db = pymysql.connect(user="root", password="bkex.com", host=self.data_url,
                                          database=self.database,
                                          port=3306, charset='utf8mb4')
        cur = db.cursor()
        return db,cur

    def query_account_only_one(self,userId):
        '''获取用户最新的一条账单'''
        db,cur = self.connect_db()
        try:
            sql = '''SELECT * FROM tbl_user_ex_account WHERE user_id ={user_id} ORDER BY update_time DESC '''.format(user_id=userId)
            cur.execute(sql)
            db.commit()
            return cur.fetchone()
        finally:
            cur.close()

    def query_lock_record(self):
        '''获取最新一条活期宝存入数据'''
        db, cur = self.connect_db()
        try:
            sql = """SELECT * FROM `tbl_lock_record` ORDER BY `create_time` DESC """
            cur.execute(sql)
            db.commit()
            return cur.fetchone()
        finally:
            cur.close()

    def update_lock_record_time(self):
        '''把时间更新为昨天'''
        data=self.query_lock_record()
        create_time = data[-3]
        id = data[0]
        # 未完成

if __name__ == "__main__":
    ins = InitDatabase()
    print(ins.query_lock_record())