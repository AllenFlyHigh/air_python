import sys
import os
dir=os.path.abspath('..')
sys.path.append(dir)

from apscheduler.schedulers.background import BlockingScheduler
from utils.crawl_data.my_crawl_data import get_craw_data
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
import time
from utils.logging.getLogger import GetLogger
from queue import Queue
from utils.http_util.sendMsgToGo import sendMsgToGo
#定义队列和日志
myQueue = Queue()
#此时的路径是相对于调用者的路径
logger = GetLogger(logs_dir='./logs').get_logger()
scheduler = BlockingScheduler()

#网页爬取数据任务
def craw_task():
    get_craw_data()
    logger.info("数据抓取成功!")
    myQueue.put(1)
#模型计算任务
def make_prediction():
    while myQueue.empty() == True:
        #如果没有抓取到数据，是不会进行预测
        time.sleep(1)
    myQueue.get()
    logger.info("模型计算完成！")
    myQueue.task_done()
    sendMsgToGo()
#监控任务
def my_listener(event):
    if event.exception:
        #如果出现问题，直接shutdown，并发送一个消息给gin server，
        # 同时将错误写进日志中
        logger.error("定时任务出现错误，python端终止!")
        scheduler.shutdown()
    else:
        logger.info("数据抓取和模型计算任务正常!")
#定时任务
def cronTask():
    scheduler.add_job(
        craw_task,
        trigger='cron',
        second='*/20',
    )
    #
    scheduler.add_job(
        make_prediction,
        trigger='cron',
        second='*/20'
    )

    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler.start()

if __name__ == '__main__':
    cronTask()