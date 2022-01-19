from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


from selenium.webdriver.common.by import By

def get_driver_for_Chrome():
	from webdriver_manager.chrome import ChromeDriverManager
	driver = webdriver.Chrome(ChromeDriverManager().install())
	return driver

def get_driver_for_Firefox():
	from webdriver_manager.firefox import GeckoDriverManager
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
	return driver

def get_driver(browser_name):
	if browser_name == "Firefox":
		return get_driver_for_Firefox()
	else:
		return get_driver_for_Chrome()

driver = get_driver("chrome")
driver.get("http://127.0.0.1:8000/")
driver.maximize_window()

login = driver.find_element_by_xpath('/html/body/div[2]/div[2]/a[2]')
login.click()

time.sleep(1)

username = driver.find_element_by_xpath('//*[@id="user"]')
username.clear()
username.send_keys("011181076")

password = driver.find_element_by_xpath('//*[@id="password"]')
password.clear()
password.send_keys("kisuna")

login = driver.find_element_by_xpath('/html/body/form/input[2]')
login.click()

time.sleep(1)

project_registration_btn = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/a[2]')
project_registration_btn.click()

time.sleep(2)

file = open('input_add_project_members.txt','r', encoding = 'utf-8')
lines = file.readlines()
file.close()

file = open('output_add_project_members.txt','w', encoding = 'utf-8')
for line in lines:
    line = line.split(':')

    student_id_box = driver.find_element_by_xpath('//*[@id="student_id"]')
    student_id_box.clear()
    for x in line[0]:
        student_id_box.send_keys(x)
        time.sleep(0.05)
    time.sleep(0.5)

    line[1] = line[1][:-1]

    project_members = driver.find_element_by_xpath('//*[@id="project_members"]')
    project_members = project_members.text
    project_members = project_members.split(',')
    len_project_members = len(project_members)
    if len(project_members[0])==0:
        len_project_members = 0

    add_member_btn = driver.find_element_by_id('add_member')
    add_member_btn.click()

    received_output =  len(driver.find_element_by_xpath('//*[@id="project_members"]').text.split(','))
    if len_project_members == received_output:
        received_output = "Not Added"
    else:
        received_output = "Added"

    if line[1] == received_output:
        file.write(f'OUTPUT OK FOR INPUT: {line[0]}\n')
    else:
        file.write(f'OUTPUT MISMATCH FOR INPUT: {line[0]},\nExpected output: {line[1]}, Received output: {received_output}\n')
    time.sleep(0.5)
file.close()
