import time
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
import pytest
from allure_commons.types import AttachmentType
import allure
from pageObjects.BaseClass import BaseClass
class SearchCustomer(BaseClass):
    
    #Add Customer
    txtEmail_Id="SearchEmail"
    txtFirstName_Id="SearchFirstName"
    txtLastName_Id="SearchLastName"
    btnSearch_Id="search-customers"
    
    #table
    table_Search_Results = "//table[@role='grid']"
    table_Xpath = "//table[@id='customers-grid']"
    table_row_Results = "//table[@id='customers-grid']//tbody//tr[@role='row']"
    table_Column_Results = "//table[@id='customers-grid']//tbody//tr//td"
    lnkCustomers_Menuitem_xpath= "(//span[@class='menu-item-title'][contains(text(),'Customers')])[1]"
    
  
    
    

        
    def click_On_Xpath(self,xpath):
        time.sleep(1)
        self.driver.find_element_by_xpath(xpath).click()
    
    def set_Text_Id(self,id,value):
        self.driver.find_element_by_id(id).clear()
        self.driver.find_element_by_id(id).send_keys(value)
    
    def click_On_Id(self,id):
        self.driver.find_element_by_id(id).click()
        
    def getLength(self,xpath):
        return len(self.driver.find_elements_by_xpath(xpath))
    def SearchCustomerByEmail(self,xpath,Email):
        flag=False
        for r in range(1,self.getLength(xpath)+1):
            table = self.driver.find_element_by_xpath(self.table_Xpath)
            emailid= table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[2]").text
            if emailid == Email:
                flag = True
                break
            return flag
    
    def SearchCustomerByData(self,xpath,Data):
        flag=False
        length = self.getLength(xpath)
        for r in range(1,length+1):
            table = self.driver.find_element_by_xpath(self.table_Xpath)
            if "@" in Data:
                emailid= table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[2]").text
                if emailid == Data:
                    flag = True
                    break
            elif not "@" in Data:
                emailid= table.find_element_by_xpath("//table[@id='customers-grid']//tbody//tr["+str(r)+"]//td[3]").text
                if emailid == Data:
                    flag = True
                    break
            else:
                    flag = True
        return flag
                
    def set_dropdown_Xpath(self,xpath,value):
            dropdown = Select(self.driver.find_element_by_xpath(xpath))
            dropdown.select_by_visible_text(value)
    
       
    def __init__(self,driver):
        self.driver= driver
        super().__init__(driver)
        self.page=BaseClass(self)
    
    
    
    