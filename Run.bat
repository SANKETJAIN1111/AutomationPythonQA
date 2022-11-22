cd \
D:
cd D:\AutomationPythonQA\AutomationPython
python -m pytest -s -v -n=2 -m sanity --alluredir="D:\AutomationPythonQA\AutomationPython\Reports\Allure-Reports" D:\AutomationPythonQA\AutomationPython\testCases --browser chrome
REM python -m pytest -s -v --alluredir="D:\AutomationPythonQA\AutomationPython\Reports\Allure-Reports" D:\AutomationPythonQA\AutomationPython\testCases\test_Login.py --browser firefox
REM python -m pytest -v -s -m "sanity" --html=Reports\Customers1_report2.html testCases\ --browser firefox
REM python -m pytest -v -s -m "regression" --html=Reports\Customers1_report2.html testCases\ --browser firefox
REM python -m pytest -v -s -m "sanity or regression" --html=Reports\Customers1_report2.html testCases\ --browser firefox
REM python -m pytest -v -s -m "sanity And regression" --html=Reports\Customers1_report2.html testCases\ --browser firefox