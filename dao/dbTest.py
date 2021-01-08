import MySQLdb
import sys
import os
dir=os.path.abspath('..')
sys.path.append(dir)
from utils.logging.getLogger import GetLogger
logger = GetLogger(logs_dir='../logs').get_logger()
class DBTest:
    def __init__(self, db):
        self.db = db
    def selectTest(self):
        cursor = self.db.cursor()
        sql = "select * from user"
        try:
            logger.info("执行了" + sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            for row in results:
                userName = row[1]
                password = row[2]
                print(type(userName))
                print(userName + ":" + password)
            logger.info("sql 操作正确")
            # db.commit()
        except:
            logger.info(sql + "执行错误")
            print("出现了错误!")
            self.db.rollback()
        self.db.close()
    def insertTest (self):
        cursor = db.cursor()
        id = 4
        username = 'pythontest'
        email = '2969141711@qq.com'
        phone = '18816209319'
        sex = 1
        role_id = 1
        sql = "INSERT INTO USER VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
              (id, username, username, username, email,phone, sex, role_id)
        try :
            cursor.execute(sql)
            db.commit()
        except:
            print('出现错误，回滚')
            db.rollback()
        db.close()

if __name__ == '__main__':

    db = MySQLdb.connect("localhost", "root", "root123", "air", charset="utf8")
    dtest = DBTest(db)

    dtest.selectTest()


