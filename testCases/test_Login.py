'''
Created on Nov 26, 2020

@author: 52128856(Sanket Jain )
'''
import time
from datetime import datetime
from pageObjects.LoginPage import LoginPage
from Utilities.readproperties import ReadConfig
import pytest
import allure
from allure_commons.types import AttachmentType
from Utilities import ExcelUtils
import os
from Utilities.JsonData import JsonData
import allure_pytest
from pageObjects.BaseClass import BaseClass
import pageObjects.BaseClass
@allure.severity(allure.severity_level.NORMAL)
class Test_Login():
    pass

    '''
    classdocs

    '''
#     baseUrl = ReadConfig.get_ApplicationURl()
#     username = ReadConfig.get_ApplicationUsername()
#     password = ReadConfig.get_ApplicationPassword()
#     logger = LogGen.loggen()
    @allure.feature("Home Page Failure")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.Xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_001_homePageTitle(self,setup):
        self.driver = setup
#         self.driver = BaseClass.BrowserLaunch()
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
        self.page = LoginPage(self.driver)
        self.page.ReportLogger("Test Case Home Page Title ")
        self.page.Title("Your store. Login1")
        
    @allure.feature("Home Page")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_002_homePageTitle(self,setup):
        
        try:
            self.driver = setup
            Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
            Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
            fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
            testclass = fulltestname.split("::")[0].split('.py')[0]
            testcase = fulltestname.split(":")[-1].split(' ')[0]
            testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
            username=testdata.get("username")
            password=testdata.get("password")
            self.page = LoginPage(self.driver)
            self.page.ReportLogger("Test Case Home Page Title ")
            self.page.Title("Your store. Loginl")
        except AssertionError: 
            self.page.ReportLogger("Assertion False")  
#         act_title = self.driver.title
#         print(act_title)
#         if act_title=="Your store. Login":
#             assert True
#             self.logger.info(" Home Page title test is Pass")
#         else:
#             allure.attach(self.driver.get_screenshot_as_png(), name=".\\Screenshots\\"+datetime.now().strftime("%d%m%Y%H%M%S")+"test_Login.png", attachment_type= AttachmentType.PNG)
#             self.logger.info("Testcase Home Page is Failed")
#             assert False

             
    @allure.title("test_loginPage")
    @allure.feature("Login Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_002_loginPage(self,setup):
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.ReportLogger("test Login Page Title")
    
        time.sleep(1)
        self.lp.Login(username,password)
        self.lp.Title("Dashboard / nopCommerce administration")
    
    @allure.title("test login Page Skipped")
    @allure.feature("Login Page Skipped")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.skip
    @pytest.mark.regression
    def test_001_loginPage(self,setup):
#         Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
#         Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
#         self.driver = BaseClass.BrowserLaunch()
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.ReportLogger("test Login Page Title")
    
        time.sleep(1)
        self.lp.Login(username,password)
        self.lp.Title("Dashboard / nopCommerce administration")
#         act_title1= self.driver.title
#         print(act_title1)
#         if act_title1=="Dashboard / nopCommerce administration":
#             assert True
#         else:
#             allure.attach(self.driver.get_screenshot_as_png(), name=".\\Screenshots\\"+datetime.now().strftime("%d%m%Y%H%M%S")+"test_Login.png", attachment_type= AttachmentType.PNG)
# #             self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
#             self.logger.info("Testcase Home Page is Failed")
#             assert False
#         def test_with_scoped_finalizers(self,
#                                     function_scope_fixture_with_finalizer,
#                                     class_scope_fixture_with_finalizer,
#                                     module_scope_fixture_with_finalizer,
#                                     session_scope_fixture_with_finalizer):
#             step_inside_test_body()
        '''
        Constructor
        '''
        def __init__(self, driver): 
            super().__init__(self, driver) 
                # invoking the __init__ of the parent class  
                