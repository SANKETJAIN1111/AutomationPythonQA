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
class Test_Login_DDT():
    '''
    classdocs

    '''
#     logger = get_logger()
#     baseUrl = ReadConfig.get_ApplicationURl()
  
#     reportpath = ReadConfig.get_ApplicationReport()
    #username = ReadConfig.get_ApplicationUsername()
    #password = ReadConfig.get_ApplicationPassword()
    @allure.title("test Home Page")
    @allure.feature("Home Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.regression
    def test_homePageTitle_ddt(self,setup):
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.ReportLogger("************Test 001 DDT Login *************")
        self.lp.ReportLogger("************Verify Home Page **********")
#              Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
#         act_title = self.driver.title
        self.lp.Title("Your store. Login1")
#         print(act_title)
#         if act_title=="Your store. Login1":
#             assert True
#             self.lp.ReportLogger(" Home Page title test is Pass ")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\"+ datetime.now().strftime("%d%m%Y%H%M%S")+" test_homePageTitle.png")
#             self.lp.ReportLogger("Testcase Home Page is Failed")
#             assert False

    @allure.title("test_loginPage")
    @allure.feature("Login Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity  
    def test_loginPage_ddt(self,setup):
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.ReportLogger("************Test 002 DDT Login *************")
        self.lp.ReportLogger("************Verify Login Page **********")
#              Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
        self.exp=testdata.get("exp")
        self.lp.ReportLogger("test Login Page Title")
    
        time.sleep(1)
        self.lp.Login(username,password)
#         self.driver = setup
# #         self.driver.get(self.baseUrl)
#         self.lp = LoginPage(self.driver)
#         time.sleep(1)
#         self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
#         print("Number of Row i a Excel:", self.rows)
        lst_status = []#empty list variable
        act_title1= self.driver.title
        exp_tittle= "Dashboard / nopCommerce administration"
#         
#         for r in range(2,self.rows+1):
#             self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
#             self.passwordexcel = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
#             self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
#             time.sleep(2)
#             self.lp.setUserName(self.user)
#             time.sleep(1)
#             self.lp.setPassword(self.passwordexcel)
#             time.sleep(1)
#             self.lp.clickLogin()
#             time.sleep(1)
           
         
        if act_title1 == exp_tittle:
            if  self.exp=="Pass":
                    self.lp.ReportLogger("****Passed****")
#                     self.lp.clickLogout()
                    lst_status.append("Pass")
            elif self.exp=="Fail":
                    self.lp.ReportLogger("****Failed****")
                    lst_status.append("Fail")
            elif act_title1!= self.exp:
                if self.exp=="Pass":
                    self.lp.ReportLogger("****Failed****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.lp.ReportLogger("****Passed****")
                    lst_status.append("Pass")
    
        if "Fail" not in lst_status:
            assert True
            self.lp.ReportLogger("Login DDT test Passed ...")
           
        else:
            self.lp.ReportLogger("Testcase Home Page is Failed")
           
            assert False
            
        self.lp.ReportLogger("*********************End of Login DDt Test **********") 
        self.lp.ReportLogger("******Completed TC Login  002 ")
    
#         self.lp.setUserName(self.username)
#         time.sleep(1)
#         self.lp.setPassword(self.password)
#         time.sleep(1)
#         self.lp.clickLogin()
#         act_title1= self.driver.title
#         if act_title1=="Dashboard / nopCommerce administration":
#             assert True
#             self.logger.info("****test login Page is Pass ****")
#            
#             self.logger.info("****test login Page is Pass ****")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
#            
#             self.logger.error("fail ho gaya")
#             assert False
        '''
        Constructor
        '''
        