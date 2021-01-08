import sys
import os
dir=os.path.abspath('..')
sys.path.append(dir)
from utils.mysql_util.MysqlConn import MySql
from utils.logging.getLogger import GetLogger
#注意此时的路径
logger = GetLogger(logs_dir='./logs').get_logger()

class MloutDB:
    def __init__(self):
        return
    def insertMany(self, value_list):
        mysql = MySql()
        print(value_list[0])
        sql = "INSERT INTO MLOUT(time, station_name, substance_type, prediction_value)VALUES(%s, %s, %s, %s)"
        logger.info("执行了" + sql)
        try:
            count = mysql.insertMany(sql, value_list)
            logger.info("批量插入成功！")
        except:
            logger.error("批量插入失败！")
            count = -1
        mysql.dispose()
        return count
