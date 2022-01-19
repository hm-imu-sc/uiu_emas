from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:8000/prize_giving_page/")
driver.maximize_window()

trimester = driver.find_element_by_xpath('//*[@id="trimester"]')
course = driver.find_element_by_xpath('//*[@id="courses"]')
project = driver.find_element_by_xpath('//*[@id="projects"]')
gold = driver.find_element_by_xpath('//*[@id="gold"]/label/i')
silver = driver.find_element_by_xpath('//*[@id="silver"]/label/i')
bronze = driver.find_element_by_xpath('//*[@id="bronze"]/label/i')
submit = driver.find_element_by_xpath('//*[@id="submit"]')

#test case 2 - adding prize without selecting a prize
trimester.click()
select_trimester=driver.find_element_by_xpath('//*[@id="trimester"]/option[2]')#1st trimester in the list
select_trimester.click()
course.click()
select_course=driver.find_element_by_xpath('//*[@id="courses"]/option[3]')#2nd course in the list
select_course.click()
project.click()
select_project=driver.find_element_by_xpath('//*[@id="projects"]/option[2]')#1st course in the list
prized_team=select_project.text#will be used later on another test case
select_project.click()
submit.click()
time.sleep(0.5)
msg=driver.find_element_by_xpath('//*[@id="error"]/p')
msg=msg.text

if msg == "Please select a valid prize":
    print("test case 1 - give award without selecting a prize : Success. User was asked to select a valid prize")
else:
    print("test case 1 - add random prize : Fail. Prize was added without any prize")

#test case 2 - adding a prize randomly

gold.click()
submit.click()

time.sleep(0.5)
msg=driver.find_element_by_xpath('//*[@id="error"]/p')
msg=msg.text
if msg == "Prize successfully added":
    print("test case 2 - add random prize : Success. Prize added successfully")
else:
    print("test case 2 - add random prize : Fail. Prize could not be added")

#test case 3 - spamming the give award button without changing input
flag = True
for i in range(10):
    submit.click()
    time.sleep(0.5)
    msg = driver.find_element_by_xpath('//*[@id="error"]/p')
    msg = msg.text
    if msg=="Prize successfully added":
        flag=False
if flag:
    print("test case 3 - spam give award button : Success. Prize was not added.")
else:
    print("test case 3 - spam give award button : Fail. Prize was added again")

#test case 4 - trying to give the team who already won a prize a second prize
gold.click()
submit.click()

time.sleep(0.5)
msg=driver.find_element_by_xpath('//*[@id="error"]/p')
msg=msg.text
if msg == "Team already won a prize":
    print("test case 4 - give same team who won before another prize : Success. User was notified that the team had already won a prize")
else:
    print("test case 4 - give same team who won before another prize : Fail. Gave the team another prize.")

#test case 5 - setting invalid trimester value
trimester.click()
select_trimester=driver.find_element_by_xpath('//*[@id="trimester"]/option[1]')#0th trimester in the list(select)
select_trimester.click()
submit.click()
time.sleep(0.5)
msg = driver.find_element_by_xpath('//*[@id="error"]/p')
msg = msg.text

if msg == "Please select a valid trimester":
    print("test case 5 - submit invalid trimester value : Success. User was asked to provide valid trimester")
else:
    print("test case 5 - submit invalid trimester value : Fail. Prize was added with invalid trimester")

#test case 6 - submit invalid course value
trimester.click()
select_trimester=driver.find_element_by_xpath('//*[@id="trimester"]/option[2]')
select_trimester.click()

course.click()
select_course=driver.find_element_by_xpath('//*[@id="courses"]/option[1]')#0th course in the list(select)
select_course.click()
submit.click()
time.sleep(0.5)
msg = driver.find_element_by_xpath('//*[@id="error"]/p')
msg = msg.text

if msg == "Please select a valid course":
    print("test case 6 - submit invalid course value : Success. User was asked to provide valid course")
else:
    print("test case 6 - submit invalid course value : Fail. Prize was added with invalid course")

#test case 7 - submit invalid team name
trimester.click()
select_trimester=driver.find_element_by_xpath('//*[@id="trimester"]/option[2]')
select_trimester.click()
course.click()
select_course=driver.find_element_by_xpath('//*[@id="courses"]/option[2]')
select_course.click()

project.click()
select_project=driver.find_element_by_xpath('//*[@id="projects"]/option[1]')#0th course in the list(select)
select_project.click()
submit.click()
time.sleep(0.5)
msg = driver.find_element_by_xpath('//*[@id="error"]/p')
msg = msg.text

if msg == "Please select a valid team name":
    print("test case 7 - submit invalid team name : Success. User was asked to provide valid team name")
else:
    print("test case 7 - submit invalid team name : Fail. Prize was added with invalid team name")

#test case 8 - trying to select the team who already won a prize
trimester.click()
select_trimester=driver.find_element_by_xpath('//*[@id="trimester"]/option[2]')#1st trimester in the list
select_trimester.click()
course.click()
select_course=driver.find_element_by_xpath('//*[@id="courses"]/option[3]')#2nd course in the list
select_course.click()
project.click()
select_project=driver.find_element_by_xpath('//*[@id="projects"]/option[2]')#1st course in the list

if select_course.text != prized_team:
    print("test case 8 - select team with previous prize : Success. Team name not in team name list")
else:
    print("test case 8 - select team with previous prize : Fail. Selected team was prized before")

