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

elementClub = driver.find_element_by_id('club_name_filter')
# load the drop down -> club name
elementClub.click()
drpClubName = Select(elementClub)

# select value of dropdown -> club name
selectedValClubName = 'UIU Computer Club'
drpClubName.select_by_value(selectedValClubName)
time.sleep(2)


elementYear = driver.find_element_by_id('year_filter')
# load the drop down -> year
elementYear.click()
drpYear = Select(elementYear)

# select value of dropdown -> year
selectedValYear = '2022'
drpYear.select_by_value(selectedValYear)
btn = driver.find_element_by_name('filter')
time.sleep(2)

# click the filter button
btn.click()

elementDivClubName = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]')
elementDivYear = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/h1/div')

if (elementDivClubName.text == selectedValClubName and elementDivYear.text == selectedValYear):
    print('========= OK FOR Club Name Dropdown: Received ' + elementDivClubName.text + ', Expected ' + selectedValClubName);
    print('========= OK FOR Year Dropdown: Received ' + elementDivYear.text + ', Expected ' + selectedValYear);
else:
    print('========= Fail FOR Club Name Dropdown: Received ' + elementDivClubName.text + ', Expected ' + selectedValClubName);
    print('========= Fail FOR Year Dropdown: Received ' + elementDivYear.text + ', Expected ' + selectedValYear);
time.sleep(6)

x = input()

