import sys
import os
dir=os.path.abspath('..')
sys.path.append(dir)
from utils.cron_util.cronTask import cronTask
from utils.logging.getLogger import GetLogger
from utils.make_predicitions.predictions_to_database import mypreditions_to_database
logger = GetLogger(logs_dir='./logs').get_logger()

if __name__ == '__main__':
    logger.info("空气质量预测API-Python端服务启动！")
    cronTask()
    #mypreditions_to_database()