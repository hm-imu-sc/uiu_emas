from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:8000/club_ff/archive_cff_booths_page/")
driver.maximize_window()
time.sleep(2)

element = driver.find_element_by_id('club_name_filter')
#load the drop down -> club name
element.click()
drp = Select(element)

#select value of dropdown
selectedVal1 = 'UIU Computer Club'
drp.select_by_value(selectedVal1)

btn = driver.find_element_by_name('filter')

#click the filter button
btn.click()

elementDiv = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]')
if (elementDiv.text == selectedVal1):
	print('========= OK FOR Dropdown: Received ' +  elementDiv.text + ', Expected ' + selectedVal1 )
else:
	print('========= OK FOR Dropdown: Received ' +  elementDiv.text + ', Expected ' + selectedVa1 )
time.sleep(2)
    
#select null value  
selectedVal = ''
drp.select_by_value(selectedVal)    
btn.click()
time.sleep(3)

#select value of dropdown
selectedVal2 = 'UIU App Forum'
drp.select_by_value(selectedVal2)
btn.click()
elementDiv = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]')
if (elementDiv.text == selectedVal2):
	print('========= OK FOR Dropdown: Received ' +  elementDiv.text + ', Expected ' + selectedVal2 )
else:
	print("------------Test case failed! Expected: " + elementDiv.text + "Received: " + selectedVal2) 
time.sleep(1)

x = input()

