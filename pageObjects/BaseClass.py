
import os
import glob
from datetime import datetime
import pytest
from Utilities.conduentLogger import get_logger
from selenium import webdriver
from Utilities.JsonData import JsonData
from sys import exc_info
import pytest_html

import allure_pytest

from allure_commons import reporter
import allure_commons
from allure_commons.reporter import AllureReporter
global driver
global ReportPath
global logger
global driver2
global driver1
logger = get_logger()
class BaseClass(object):
        def ReportLogger(self,args):
            logger.info(args)
            return logger
        
        def BrowserLaunch(browser):
            baseUrl=JsonData.fetch_data_from_json_single('BaseUrl')
            ReportPath=JsonData.fetch_data_from_json_single('ReportPath')
            cdriver=JsonData.fetch_data_from_json_single('ChromeDriverPath')
            fdriver=JsonData.fetch_data_from_json_single('FirefoxDriverPath')
            idriver=JsonData.fetch_data_from_json_single('IeDriverPath')
            wdriver=JsonData.fetch_data_from_json_single('WindowDriverPath')
#     baseUrl = "https://admin-demo.nopcommerce.com/"
            if browser =='chrome':
                driver= webdriver.Chrome(executable_path=cdriver)
                logger.info("Launching Chrome Browser")
            elif browser=='firefox':
                driver = webdriver.Firefox(executable_path=fdriver)
#         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
                logger.info("Launching Firefox Browser")
            elif browser=='windows':
                driver = webdriver.Remote(command_executor='http://localhost:4723',desired_capabilities={'app': r'C:/Windows/System32/Notepad.exe'})
            elif browser=='windows1':
                driver1 = webdriver.Remote(command_executor='http://localhost:4723',desired_capabilities={'app': r'C:/Windows/System32/Notepad.exe'})
            elif browser=='windows2':
                driver2 = webdriver.Remote(command_executor='http://localhost:4723',desired_capabilities={'app': r'C:/Windows/System32/Notepad.exe'})
            elif browser=='ie':
                driver = webdriver.Firefox(executable_path=fdriver)
                logger.info("Launching IE Browser")
            else:
                browser ='chrome'
                driver= webdriver.Chrome(executable_path=cdriver)
                logger.info("Launching Chrome Browser")
                logger.info("Browser not Found: Default Browser Run :" + driver.name)
            driver.implicitly_wait(10)
            driver.delete_all_cookies()
            driver.get(baseUrl)
            logger.info("launch Url : " +baseUrl)
            driver.maximize_window()    
            return driver
            
        def __init__(self,driver):
            self.driver= driver

