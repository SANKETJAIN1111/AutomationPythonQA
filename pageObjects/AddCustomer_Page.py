import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
import pytest
from allure_commons.types import AttachmentType
import allure
from pageObjects.BaseClass import BaseClass
class AddCustomer(BaseClass):
    
    #Add Customer
    lnkCustomers_Menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_Menuitem_xpath= "(//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')])[1]"
    
    #buton xpath
    btnAddnew_xpath="//a[@class='btn btn-primary']"
    
    #textbox xpath
    txtEmail_xpath= "//input[@id='Email']"
    txtPassword_xpath= "//input[@id='Password']"
    txtNewsletter_xpath= "(//div[@class='k-multiselect-wrap k-floatwrap'])[1]"
    txtCustomerRoles_xpath= "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]"
    
    #list
    lstItemAdministrators_xpath= "//li[contains(text(),'Administrators')]"
    lstItemRegisterd_xpath= "//li[contains(text(),'Registered')]"
    lstItemGuests_xpath= "//li[contains(text(),'Guests')]"
    lstItemVendors_xpath= "//li[contains(text(),'Vendors')]"
    SelectItemGuest_xpath= "//*[@id='SelectedCustomerRoleIds_taglist']//li//span[2]"
    
    drpmgrOfVendors_xpath= "//*[@id='VendorId']"
    drpNewsletter_Xpath = "//*[@class='k-item'][contains(text(),'Test store 2')]"
    
    rdMaleGender_id = "//input[@id='Gender_Male']"
    rdFemaleGender_id = "//input[@id='Gender_Female']"
    
    checkbox_Is_tax= "//input[@id='IsTaxExempt']"
    
    txtFirstName_xpath= "//input[@id='FirstName']"
    txtLastName_xpath= "//input[@id='LastName']"
    txtDob_xpath=  "//input[@id='DateOfBirth']"
    txtCompanyName_xpath= "//input[@id='Company']"
    txtAdminComment_xpath=  "//textarea[@id='AdminComment']"
    btn_Save_xpath = "//button[@name='save']"
    

        
    def click_On_Xpath(self,xpath):
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath).click()
    
    def set_Text_Xpath(self,xpath,value):
        self.driver.find_element_by_xpath(xpath).clear()
        self.driver.find_element_by_xpath(xpath).send_keys(value)
        
    def set_Roles_Xpath(self,xpath):
        if xpath != '':
            self.listItem = self.driver.find_element_by_xpath(xpath)
        else:
            self.listItem = self.driver.find_element_by_xpath(self.lstItemGuests_xpath)
            time.sleep(3)
        self.driver.execute_script("argument[0].click();", self.listItem)
        
    def set_dropdown_Xpath(self,xpath,value):
            dropdown = Select(self.driver.find_element_by_xpath(xpath))
            dropdown.select_by_visible_text(value)
    def click (self, xpath):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(element=xpath), "Element Not Found {}" +xpath)
       
    def SetText(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator), "Element Not Found : " + locator).sendKeys(locator)
    def IsEnabled(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator), "Element Not Found : " + locator)
        return bool(element)
    
    def __init__(self,driver):
        self.driver= driver
        super().__init__(driver)
        self.page=BaseClass(self)
    