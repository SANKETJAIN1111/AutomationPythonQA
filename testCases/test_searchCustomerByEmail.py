'''Created on Feb 10, 2021

@author: 52128856(Sanket Jain )
'''
import time
from datetime import datetime
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer_Page import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer
import pytest
import allure
from allure_commons.types import AttachmentType
from Utilities import ExcelUtils
import os
from Utilities.JsonData import JsonData
import allure_pytest
from pageObjects.BaseClass import BaseClass
import pageObjects.BaseClass
import allure
@allure.severity(allure.severity_level.NORMAL)
class Test_SearchCustomer_DDT():
#     baseUrl = ReadConfig.get_ApplicationURl()
#     path = ".//testData/LoginData.xlsx"
#     reportpath = ReadConfig.get_ApplicationReport()
#     logger = get_logger() #logger
    @allure.feature("Search Customer By Mail")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    def test_001_SearchCustomerByMail_ddt(self,setup):
        self.driver = setup
        self.lp = LoginPage(self.driver)
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
#         self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
#         print("Number of Row i a Excel:", self.rows)
#         
#         for r in range(2,self.rows-2):
#             self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
#             self.passwordexcel = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
#             self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
#             time.sleep(2)
#             self.page.setUserName(self.user)
#             time.sleep(1)
#             self.page.setPassword(self.passwordexcel)
#             time.sleep(1)
#             self.page.clickLogin()
#             time.sleep(1)
        
        self.lp.ReportLogger("test Search Customer By Mail Id")
        time.sleep(1)
        self.lp.Login(username,password)
        self.lp.Title("Dashboard / nopCommerce administration")
        
        self.lp.ReportLogger("Add Customer Details")  
        self.page = AddCustomer(self.driver)
        self.page.click_On_Xpath(self.page.lnkCustomers_Menu_xpath)
        self.page.click_On_Xpath(self.page.lnkCustomers_Menuitem_xpath)
        
        self.page = SearchCustomer(self.driver)
        self.page.set_Text_Id(self.page.txtEmail_Id, "victoria_victoria@nopCommerce.com")
        self.page.click_On_Id(self.page.btnSearch_Id)
        time.sleep(3)
        status= self.page.SearchCustomerByData(self.page.table_row_Results,"victoria_victoria@nopCommerce.com")
        if status == True:
            assert True == status
#             self.driver.close()
            self.lp.ReportLogger("************* Search customer info**************")
            self.lp.ReportLogger("******* Ending Search customer Test Passed************")
        else:
            assert False == status
#             self.driver.close()
    
    @allure.feature("Search Customer By Id")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.regression   
    def test_002_SearchCustomerByName_ddt(self,setup):
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        self.driver = setup
        self.lp = LoginPage(self.driver)
        self.lp.ReportLogger("************Test 002 Search Customers *************")
#         self.driver = setup
#         time.sleep(2)
#         self.page = LoginPage(self.driver)
#         self.rows = ExcelUtils.getRowCount(self.path, 'Credentials')
#         print("Number of Row i a Excel:", self.rows)
#         
#         for r in range(2,self.rows-2):
#             self.user = ExcelUtils.readData(self.path, 'Credentials', r, 1)
#             self.passwordexcel = ExcelUtils.readData(self.path, 'Credentials', r, 2)
#             self.exp = ExcelUtils.readData(self.path, 'Credentials', r, 3)
#             time.sleep(2)
#             self.page.setUserName(self.user)
#             time.sleep(1)
#             self.page.setPassword(self.passwordexcel)
#             time.sleep(1)
#             self.page.clickLogin()
#             time.sleep(1)
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
        username=testdata.get("username")
        password=testdata.get("password")
        
        
        self.lp.ReportLogger("test Search Customer By Mail Id")
        time.sleep(1)
        self.lp.Login(username,password)
        self.lp.Title("Dashboard / nopCommerce administration")
        self.lp.ReportLogger("************Login Successfully *************")  
        self.page = AddCustomer(self.driver)
        self.page.click_On_Xpath(self.page.lnkCustomers_Menu_xpath)
        self.page.click_On_Xpath(self.page.lnkCustomers_Menuitem_xpath)
        
        self.page = SearchCustomer(self.driver)
        self.page.set_Text_Id(self.page.txtFirstName_Id, "Victoria")
        self.page.click_On_Id(self.page.btnSearch_Id)
        time.sleep(3)
        status= self.page.SearchCustomerByData(self.page.table_row_Results,"Victoria Terces")
        if status == True:
            assert True == status
#             self.driver.close()
            self.lp.ReportLogger("************* Search customer info**************")
            self.lp.ReportLogger("******* Ending Search customer Test Passed************")
        else:
            assert False == status
#             self.driver.close()
            self.logger.log(msg="Test Case Fail")
        
        