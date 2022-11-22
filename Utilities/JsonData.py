import json 
from textwrap import indent
import os

    
class JsonData():
    
    def get_all_json_data():
        files = os.path.abspath('D:\\AutomationPythonQA\\AutomationPython\\Utilities\\Data.json')
        with open(files) as file:
            data = json.load(file)
        return data 
    
    def fetch_data_from_json_single(key):
        files = os.path.abspath('D:\\AutomationPythonQA\\AutomationPython\\Utilities\\Data.json')
        with open(files) as file:
            data = json.load(file)
            for Data in data['Data']:
                return Data[key]
    
    def fetch_data_from_json_double( fkey, skey):
        files = os.path.abspath('D:\\AutomationPythonQA\\AutomationPython\\Utilities\\Data.json')
        with open('testData/Data.json') as file:
            data = json.load(file)
            for Data in data['Data']:
                return Data[fkey], Data[skey]
        
    def delete_data_from_json_single(self, key):
        files = os.path.abspath('D:\\AutomationPythonQA\\AutomationPython\\Utilities\\Data.json')
        with open('testData/Data.json') as file:
            data = json.load(file)
            for Data in data['Data']:
                del Data[key]
            
    def write_data_from_json_single(self, key):
        files = os.path.abspath('D:\\AutomationPythonQA\\AutomationPython\\Utilities\\Data.json')
        with open('Data.json','w') as file:
            data = json.dump(key, file)
    
    def write_data_from_json_single(self, key):
        files = os.path.abspath('D:\\AutomationPythonQA\\AutomationPython\\Utilities\\Data.json')
        with open('Data.json','w') as file:
            data = json.dump(key, file, indent=2)
            
