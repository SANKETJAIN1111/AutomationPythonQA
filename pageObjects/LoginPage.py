from datetime import datetime
import pytest
from allure_commons.types import AttachmentType
import allure
import allure_commons
from pageObjects.BaseClass import BaseClass
# logger = BaseClass.ReportLogger(args)
class LoginPage(BaseClass):
    
#     self.page = BaseClass(driver)
#     self.page.ReportLogger("Test Case Home Page Title ")
    textbox_username_id="Email"
    textbox_password_id="Password"
    button_login="//button[@class='button-1 login-button']"
    link_logout_link_Test="Logout"
    @allure.step
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
        self.page.ReportLogger("Enter Username "+username)
    @allure.step
    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
        self.page.ReportLogger("Enter Password  "+password)
    @allure.step
    def clickLogin(self):
        value = self.driver.find_element_by_xpath(self.button_login).is_enabled()
        if value==True:
            element= self.driver.find_element_by_xpath(self.button_login).text
            self.driver.find_element_by_xpath(self.button_login).click()
            self.page.ReportLogger("Click On Button "+ element)
        else:
            self.page.ReportLogger("Control Not Found "+ element)
    @allure.step
    def clickLogout(self):
        value = self.driver.find_element_by_xpath(By.XPATH, self.link_logout_link_Test).is_enabled()
        if value==True:
            element= self.driver.find_element_by_xpath(self.link_logout_link_Test).text
            self.driver.find_element_by_xpath(self.link_logout_link_Test).click()
            self.page.ReportLogger("Click On Button "+element)
        else:
            self.page.ReportLogger("Control Not Found "+element)
    @allure.step
    def Login(self, username, password):
        self.setUserName(username)
        self.setPassword(password)
        self.clickLogin()
    @allure.step
    def Title(self,expectedtitle):
        act_title = self.driver.title
        print(act_title)
        if act_title==expectedtitle:
            assert True
            self.page.ReportLogger("Expected : "+expectedtitle+" Actual: "+ act_title )
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name=".\\Screenshots\\"+datetime.now().strftime("%d%m%Y%H%M%S")+"test_Login.png",attachment_type= AttachmentType.PNG)
#             allure.attach(self.driver.get_screenshot_as_png(), name=".\\Screenshots\\"+datetime.now().strftime("%d%m%Y%H%M%S")+"test_Login.png", attachment_type= AttachmentType.PNG)
            self.page.ReportLogger("Expected : "+expectedtitle+" Actual: "+ act_title )
#             assert False 
   
    def ReportLogger(self,args):
        self.page.ReportLogger(args)
        
    def __init__(self,driver):
        self.driver= driver
        super().__init__(driver)
        self.page=BaseClass(self)