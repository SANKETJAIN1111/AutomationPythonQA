'''
Created on Nov 26, 2020

@author: 52128856
'''
import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig():
    '''
    classdocs
    '''
    
    @staticmethod
    def get_Chrome_Browser():
        driver = config.get('common info', 'chromeBrowserPath')
        return driver
    
    @staticmethod
    def get_Firefox_Browser():
        driver = config.get('common info', 'firefoxBrowserPath')
        return driver
    
    @staticmethod
    def get_IE_Browser():
        driver = config.get('common info', 'ieBrowserPath')
        return driver
    
    @staticmethod
    def get_ApplicationURl():
        url = config.get('common info', 'baseUrl')
        return url
    
    @staticmethod
    def get_ApplicationTestData():
        testData = config.get('common info', 'testDataPath')
        return testData
    
    @staticmethod
    def get_ApplicationReport():
        reportPath = config.get('common info', 'reportPath')
        return reportPath
    
    @staticmethod
    def get_ApplicationUsername():
        username = config.get('common info', 'username')
        return username
    
    @staticmethod
    def get_ApplicationPassword():
        password = config.get('common info', 'password')
        return password
    
    def __init__(self, params):
        '''
        Constructor
        '''
        