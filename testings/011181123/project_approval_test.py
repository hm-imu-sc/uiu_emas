from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://localhost:8000/")
# print(driver.title)
driver.maximize_window()
link1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/a[2]") #for login_page
link1.click()

inp1 = driver.find_element_by_xpath('//*[@id="user"]') #for User ID
inp1.send_keys('SS')

inp2 = driver.find_element_by_xpath('//*[@id="password"]') #for password
inp2.send_keys('password')

submit_btn = driver.find_element_by_xpath("/html/body/form/input[2]") #for login button
submit_btn.click()
time.sleep(2)

link2 = driver.find_element_by_xpath('//*[@id="appr_pen_proj"]') # for approve pending projects
link2.click()

time.sleep(2)
project_count = driver.find_elements(By.CSS_SELECTOR, ".project")

project_count = len(project_count)

for i in range(project_count):
	project = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/span[1]')
	project_name = project.text

	expand_btn = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div/a')
	expand_btn.click()

	approve_btn = driver.find_element_by_xpath('/html/body/a')
	approve_btn.click()

	time.sleep(1)

	approved_projects = driver.find_elements(By.CSS_SELECTOR,".project-name")
	found = False
	for approve_project in approved_projects:
		if project_name == approve_project.text:
			found = True
			break

	if found == False:
		print(f'OUTPUT MISMATCH FOR INPUT: {project_name},\nExpected output: Found {project_name} in Approved Projects, Received output: Not found {project_name} in Approved Projects')
	else:
		print(f'OUTPUT OK FOR INPUT: {project_name}')

	if i != (project_count-1):
		project_approval_btn = driver.find_element_by_xpath('//*[@id="appr_pen_proj"]')
		project_approval_btn.click()

	time.sleep(2)
