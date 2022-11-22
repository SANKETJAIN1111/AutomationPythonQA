'''
Created on Nov 26, 2020

@author: 52128856
'''
import os
import glob
from datetime import datetime
import pytest
from selenium import webdriver
from Utilities.JsonData import JsonData
from sys import exc_info
import pytest_html
from _pytest.reports import BaseReport
from _pytest.runner import pytest_terminal_summary
import allure_pytest

from allure_commons import reporter
import allure_commons
from allure_commons.reporter import AllureReporter
from setuptools.config import read_configuration, configuration_to_dict
from pageObjects.BaseClass import BaseClass
global driver
global ReportPath


@pytest.yield_fixture()
def setup(browser):
        browser='chrome'
        driver = BaseClass.BrowserLaunch(browser)
        yield driver
        driver.close()
        page = BaseClass(driver)
        page.ReportLogger("Browser And Driver Closeed !!!!!")
#     baseUrl=JsonData.fetch_data_from_json_single('BaseUrl')
#     ReportPath=JsonData.fetch_data_from_json_single('ReportPath')
#     cdriver=JsonData.fetch_data_from_json_single('ChromeDriverPath')
#     fdriver=JsonData.fetch_data_from_json_single('FirefoxDriverPath')
#     idriver=JsonData.fetch_data_from_json_single('IeDriverPath')
# #     baseUrl = "https://admin-demo.nopcommerce.com/"
#    
#     browser='chrome'
#     if browser =='chrome':
#         driver= webdriver.Chrome(executable_path=cdriver)
#         logger.info("Launching Chrome Browser")
#     elif browser=='firefox':
#         driver = webdriver.Firefox(executable_path=fdriver)
# #         driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#         logger.info("Launching Firefox Browser")
#     elif browser=='ie':
#         driver = webdriver.Firefox(executable_path=fdriver)
#         logger.info("Launching IE Browser")
#     else:
#         logger.info("Browser not Found: :" + driver.name)
#     driver.implicitly_wait(10)
#     driver.delete_all_cookies()
#     driver.get(baseUrl)
#     logger.info("launch Url : " +baseUrl)
#     driver.maximize_window()    
    
# #     addFinalizer()
# filepath="D:\\AutomationPythonQA\\AutomationPython\\Allure.bat"
# os.get_exec_path(filepath)
@pytest.fixture(params=[True, False], ids=['param_true', 'param_false'])
def function_scope_fixture_with_finalizer(request):
    if request.param:
        print('True')
    else:
        print('False')
    def function_scope_finalizer():
        function_scope_step()
    request.addfinalizer(function_scope_finalizer)


@pytest.fixture(scope='class')
def class_scope_fixture_with_finalizer(request):
    def class_finalizer_fixture():
        class_scope_step()
    request.addfinalizer(class_finalizer_fixture)


@pytest.fixture(scope='module')
def module_scope_fixture_with_finalizer(request):
    def module_finalizer_fixture():
        module_scope_step()
    request.addfinalizer(module_finalizer_fixture)


@pytest.fixture(scope='session')
def session_scope_fixture_with_finalizer(request):
    def session_finalizer_fixture():
        session_scope_step()
    request.addfinalizer(session_finalizer_fixture)


# class TestClass(object):


        
   
        
# @pytest_sessionfinish
# def session_sessionfinish():
#      if os.path.exists("D:\\AutomationPythonQA\\AutomationPython\\Reports\\Allure-Reports\\"):
#        filepath="D:\\AutomationPythonQA\\AutomationPython\\Allure.bat"
#        os.get_exec_path(filepath)
#      else:
#         print("The file does not exist")
# @pytest.hookimpl(trylast=True)
# def pytest_sessionfinish(exitstatus):
#       timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#       os.chdir("./Reports")
#       os.mkdir(timestamp)
#       print(timestamp)
#       yield
#       shutil.move(config.option.htmlpath, "./%s/test_report.html" % timestamp)
#       
def pytest_addoption(parser): 
    parser.addoption("--browser")  
 
@pytest.fixture() 
def browser(request):
    return request.config.getoption("--browser")
#It's hook for adding Environment info to HTML Report
##########################Pytest HTML Reports############################################
def pytest_configure(config):
    config._metadata['Project Name'] = 'Conduent'
    config._metadata['Module Name'] = 'Automation'
    config._metadata['Tester']='Sanket jain'

@pytest.hookimpl(tryfirst=True)
@allure_commons.hookimpl
def pytest_configure(config):
    reports_dir =  JsonData.fetch_data_from_json_single('ReportPath')
#     if os.path.exists("D:\\AutomationPythonQA\\AutomationPython\\Reports\\Allure-Reports\\"):
#         files = glob.glob('D:\\AutomationPythonQA\\AutomationPython\\Reports\\Allure-Reports\\**\\*.*', recursive=True)
#         for f in files:
#             try:
#                 os.remove(f)
#             except OSError as e:
#                 print("Error: %s : %s" % (f, e.strerror))
#     
    if not config.option.htmlpath:
        now = datetime.now()
        # create report target dir
        # custom report file
        report = reports_dir +__name__+f"report_{datetime.now().strftime('%d%m%Y%H%M%S')}.html"
        # adjust plugin options
        config.option.htmlpath = report
        print(report)
        config.option.self_contained_html = True

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA-HOME", None)
    metadata.pop("Plugins", None)