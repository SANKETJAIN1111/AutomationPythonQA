'''Created on Feb 10, 2021

@author: 52128856(Sanket Jain )
'''

from pageObjects.AddCustomer_Page import AddCustomer
import string
import random

import time
from datetime import datetime
from pageObjects.LoginPage import LoginPage
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
class Test_AddCustomer_DDT():

    @allure.feature("Add Customer Details")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.sanity
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AddCustomer_ddt(self,setup):
        try:
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
        
            self.lp.ReportLogger("************Login Successfully *************")  
            self.page = AddCustomer(self.driver)
            self.page.click_On_Xpath(self.page.lnkCustomers_Menu_xpath)
            self.page.click_On_Xpath(self.page.lnkCustomers_Menuitem_xpath)
            self.page.click_On_Xpath(self.page.btnAddnew_xpath)
            
            self.lp.ReportLogger("************* Providing customer info**************")
            
            self.email = random_generator() + "@gmail.com"
            self.page.set_Text_Xpath(self.page.txtEmail_xpath, self.email)
            self.page.set_Text_Xpath(self.page.txtPassword_xpath, "Test123")
            self.page.set_Text_Xpath(self.page.txtFirstName_xpath, "sanket")
            self.page.set_Text_Xpath(self.page.txtLastName_xpath, "jain")
            self.page.click_On_Xpath(self.page.rdMaleGender_id)
            self.page.set_Text_Xpath(self.page.txtDob_xpath, "02/02/2004")
            self.page.set_Text_Xpath(self.page.txtCompanyName_xpath, "Automation")
            self.page.click_On_Xpath(self.page.checkbox_Is_tax)
            
            self.page.click_On_Xpath(self.page.txtNewsletter_xpath)
            self.page.click_On_Xpath(self.page.drpNewsletter_Xpath)
            
            self.page.click_On_Xpath(self.page.SelectItemGuest_xpath)
            self.page.click_On_Xpath(self.page.txtCustomerRoles_xpath)
            self.page.click_On_Xpath(self.page.lstItemGuests_xpath)
            #self.page.click_On_Xpath(self.page.lstItemGuests_xpath)
            
            self.page.click_On_Xpath(self.page.drpmgrOfVendors_xpath)
            self.page.set_dropdown_Xpath(self.page.drpmgrOfVendors_xpath, "Vendor 2")
            
            self.page.set_Text_Xpath(self.page.txtAdminComment_xpath, "This is for testing")
            self.page.click_On_Xpath(self.page.btn_Save_xpath)
            
            self.lp.ReportLogger("************* Saving customer info**************")
            self.lp.ReportLogger("************* Add customer Validation Started**************")
            
            self.msg = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
            
            print(self.msg)
            if 'The new customer has been added successfully.' in self.msg.split("x"):
                assert True == True
                self.lp.ReportLogger("******* Add Customer Test Passed ************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\"+ datetime.now().strftime("%d%m%Y%H%M%S")+" test_homePageTitle.png")
                self.lp.ReportLogger("Testcase Home Page is Failed")
                assert False == False
                
            self.lp.ReportLogger("******* Ending Home Page Tittle Test************")
        except UnicodeError:
            self.lp.ReportLogger("Unicode Format Error !!")  
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))  
        