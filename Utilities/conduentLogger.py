'''
Created on Nov 26, 2020
@author: 52128856 (Sanket Jain)
'''
import logging
import sys
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from Utilities.JsonData import JsonData

Pathname=JsonData.fetch_data_from_json_single('LoggerPath')
LOG_FILE = Pathname+"my_app"+datetime.now().strftime("%d%m%Y%H%M%S")+".log"
# LOG_FILE = ".//logs/my_app"+datetime.now().strftime("%d%m%Y%H%M%S")+".log"

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    return console_handler
def get_file_handler():
        file_handler = TimedRotatingFileHandler(LOG_FILE, when='midnight')
        return file_handler
def get_logger():
        logging.basicConfig(filename=LOG_FILE ,format='%(asctime)s: %(levelname)s: %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(get_file_handler())
        logger.addHandler(get_console_handler())
        return logger
@staticmethod
def ReportLogger(args):
        logger.info(args)
# def ReportLogger():
#     logger = get_logger()
#     return logger
#         if not getattr(logger,'handler_set',None):
#         streamHandler= logging.StreamHandler()
      
#         logger.addHandler(streamHandler)
        
#             logger.handler_set = True
        # with this pattern, it's rarely necessary to propagate the error up to parent
#         logger.propagate = False
        
# class LogGen:
#     path = ".//testData/debug.log"
#     @staticmethod
#     def loggen():
#         logging.basicConfig(filename='.//logs/my_app1.log', 
#                             level=logging.INFO, 
#                             format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')
# #         logging.basicConfig(filename= ".\\Screenshots\\"+"a.log", 
# #                             format='%(asctime)s: %(levelname)s: %(message)',
#         logger =logging.getLogger()
#         logger.setLevel(logging.INFO) 
#         logger.propagate = False
#         return logger
       
         