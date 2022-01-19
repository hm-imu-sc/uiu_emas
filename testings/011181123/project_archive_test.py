from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("http://localhost:8000/")
# print(driver.title)
driver.maximize_window()

link1= driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[2]')
link1.click()

link2 = driver.find_element_by_xpath('/html/body/div[4]/a[2]/i')
link2.click()

inp1 = driver.find_element_by_xpath('//*[@id="course_filter"]')


inp2 = driver.find_element_by_xpath('//*[@id="trimester_filter"]')

filter_btn = driver.find_element_by_xpath('//*[@id="filter"]')
