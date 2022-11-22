'''
Created on Nov 26, 2020

@author: 52128856
'''
from selenium import webdriver
import pytest

@pytest.fixture() 
def setup():
    driver = webdriver.Chrome(executable_path=".\\Utilities\\"+"chromedriver.exe")
    print("Launching Chrome Browser")
    return driver
# @pytest.fixture()
# def setup(browser):
#     if browser =='chrome':
#         driver= webdriver.Chrome()
#         print("Launching Chrome Browser")
#     elif browser=='firefox':
#         driver = webdriver.Firefox()
#         print("Launching Firefox Browser")
#     else:
#         driver = webdriver.Chrome(executable_path=".\\Utilities\\"+"chromedriver.exe")
#         print("Launching chrome Browser")
#     return driver
#  
# 
# def pytest_addoption(parser): 
#     parser.addoption("--browser")  
#     parser.addoption(browser,'chrome')
#  
# @pytest.fixture()
# def browser(request):
#    #return request.config.getoption(browser('chrome')
#     return request.config.getoption(browser,'chrome')
#It's hook for adding Environment info to HTML Report
##########################Pytest HTML Reports############################################

def pytest_configure(config):
    config._metadata['Project Name'] = 'Conduent'
    config._metadata['Module Name'] = 'Automation'
    config._metadata['Tester']='Sanket jain'
    config._metadata.pop("JAVA-HOME", None)
    config._metadata.pop("Plugins", None)
    
# Its hook for delete modify environment info to HTML report
# @pytest.mark._markers.pop()
# def pytest_metadata(metadata):
#     metadata.pop("JAVA-HOME", None)
#     metadata.pop("Plugins", None)

    

    