from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://localhost:8000/")
# print(driver.title)
driver.maximize_window()

link1= driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[2]')
link1.click()

link2 = driver.find_element_by_xpath('/html/body/div[4]/a[2]/i')
link2.click()

time.sleep(2)

file_read = open('project_archive_test_input.txt','r')
inputs = file_read.readlines()
file_read.close()

for input in inputs:
    input = input.split('-')
    expected_output = input[1][:-1]
    expected_output = expected_output.split(',')

    input = input[0]
    input = input.split(',')


    if input[0]!='NULL':
        # course selection
        course_btn = driver.find_element_by_xpath('//*[@id="course_filter"]')
        course_btn.click()
        Select(driver.find_element_by_xpath('//*[@id="course_filter"]')).select_by_value(f"{input[0]}")
        course_btn.click()

    if input[1]!='NULL':
        print(len(input[1]))
        # trimester selection
        trimester_btn = driver.find_element_by_xpath('//*[@id="trimester_filter"]')
        trimester_btn.click()

        Select(driver.find_element_by_xpath('//*[@id="trimester_filter"]')).select_by_value(f"{input[1]}")
        trimester_btn.click()

    # apply filter
    apply_filter_btn = driver.find_element_by_xpath('//*[@id="filter"]')
    apply_filter_btn.click()

    time.sleep(2)

    projects = driver.find_elements(By.CSS_SELECTOR, ".booth_thumbnail")

    correct = True

    if len(projects)!=0:
        for project in projects:
            if expected_output[0] != 'NULL':
                if expected_output[0] == project.get_attribute("course_name"):
                    continue
                else:
                    correct = False
                    break
            if expected_output[1] != 'NULL':
                if expected_output[1] == project.get_attribute("trimester"):
                    continue
                else:
                    correct = False
                    break

    if correct == True:
        print(f'OUTPUT OK FOR INPUT: {input[0], input[1]}')
    else:
        print(f'OUTPUT MISMATCH FOR INPUT: {input[0], input[1]},\nExpected output: Filtered based on {input[0], input[1]}, Received output: Not filtered based on {input[0], input[1]}')
    time.sleep(1)
