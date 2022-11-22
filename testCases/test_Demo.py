'''
Created on Nov 26, 2020

@author: 52128856(Sanket Jain )
'''
import time
from datetime import datetime
# from pageObjects.LoginPage import LoginPage
# from Utilities.readproperties import ReadConfig
import pytest
import allure
from allure_commons.types import AttachmentType
from Utilities import ExcelUtils
import os
from Utilities.JsonData import JsonData
import allure_pytest
from pageObjects.BaseClass import BaseClass
import pageObjects.BaseClass
from pywinauto.application import Application
import pywinauto
@allure.severity(allure.severity_level.NORMAL)
class Test_Demo():
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
#     @pytest.mark.Xfail(condition=lambda: True, reason='this test is expecting failure')
    def test_001_homePageTitle(self,setup):
        Sheetname=JsonData.fetch_data_from_json_single('ExcelSheetCredentials')
        Workbook =JsonData.fetch_data_from_json_single('ExcelFilePath')
        fulltestname = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        testclass = fulltestname.split("::")[0].split('.py')[0]
        testcase = fulltestname.split(":")[-1].split(' ')[0]
        driver  = setup
#         browser='windows1'
#         driver1 = BaseClass.BrowserLaunch(browser)
        
#         windows = self.driver.find_element_by_class_name('Notepad')
#         windows.find_element_by_name('Text Editor').send_keys('Hello world')
#         windows.find_element_by_name('File').click()
#         windows.find_element_by_name('Exit').click()
#         windows.find_element_by_name('Notepad').find_element_by_name("Don't Save").click()
#         
#         app =Application().start(cmd_line=u'"Notepad.exe"')
#         time.sleep(3)
#         app.Notepad.edit.type_keys('Hello world!!')
#         app.Notepad.menu_item(u'&Edit->&Replace').click()
#         app.Replace.Cancel.click()
#         app.Notepad.menu_select("File ->Exit")
#         app.Notepad.Save.click()
#         app.SaveAs.edit.set_edit_text("This is my First Demo.txt")
#         app.SaveAs.Save.click()
#         app.ConfirmSaveAs.Yes.click()
        
#         app =Application().start(cmd_line=u'"Notepad.exe"')
#         time.sleep(3)
#         windows = self.driver.find_element_by_class_name('Notepad')
#         windows.find_element_by_name('Text Editor').send_keys('Hello world')
#         windows.find_element_by_name('File').click()
#         windows.find_element_by_name('Exit').click()
#         windows.find_element_by_name('Notepad').find_element_by_name("Don't Save").click()
#         window= self.driver.find_elements_by_class_name('Notepad')
#         window = self.driver.find_element_by_name('Untitled - Notepad')
#         view_menu_item = self.driver.find_element_by_name('Application')
#         view_menu_item.find_element_by_name('Edit').click()
#         view_menu_item.find_element_by_name('Replace').click()
#         view_menu_item.click()
#         view_menu_item.find_element_by_name('History').click()
#         window.find_element_by_id('132').click()
#         window.find_element_by_id('93').click()
#         window.find_element_by_id('134').click()
#         window.find_element_by_id('97').click()
#         window.find_element_by_id('138').click()
#         window.find_element_by_id('121').click()
#         self.driver = BaseClass.BrowserLaunch()

        testdata = ExcelUtils.getData(Workbook, Sheetname,"user", "admin")
#         username=testdata.get("username")
#         password=testdata.get("password")
#         self.page = LoginPage(self.driver)
#         self.page.ReportLogger("Test Case Home Page Title ")
#         self.page.Title("Your store. Login1")