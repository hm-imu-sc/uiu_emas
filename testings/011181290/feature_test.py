
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as by
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import StaleElementReferenceException

root = "http://127.0.0.1:8080"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(root)

class TestFailed(Exception):
    pass

def print_message(str):
    print(f"\n\n{str}\n\n")

def get(css_selector, element=None):
    if element is not None:
        return element.find_elements(by.CSS_SELECTOR, css_selector)
    return driver.find_elements(by.CSS_SELECTOR, css_selector)

login_page_link = get(".utility-item .nav-item:nth-child(2)")[0]

time.sleep(1)

login_page_link.click()

u_email = "hbillah181290@bscse.uiu.ac.bd"
u_password = "password"

uname_field = get("#user")[0]
uname_field.send_keys(u_email)

pass_field = get("#password")[0]
pass_field.send_keys(u_password)

login_btn = get("input[type=\"submit\"]")[0]

time.sleep(1)

login_btn.click()

page_title = driver.title

if page_title == "student Dashboard":
    print_message("[+] Login Test Successfull !!!")
else:
    raise TestFailed
time.sleep(2)

appr_proj_btn = get("#appr_proj")[0]
appr_pen_proj_btn = get("#appr_pen_proj")[0]

appr_pen_proj_btn.click()
time.sleep(2)

projects = get(".project")
if len(projects) == 1:
    print_message("[+] Approval pending projects tab is working properly !!!")
else:
    raise TestFailed

appr_proj_btn.click()
time.sleep(2)

projects = get(".project")
if len(projects) == 3:
    print_message("[+] Approved projects tab is working properly !!!")
else:
    raise TestFailed

links = []
names = []

for project in projects:
    a = get("a", project)[0]
    links.append(a.get_attribute("href"))
    names.append(get(".project-name", project)[0].text)


score = 0
for i in range(len(links)):

    link = links[i]

    driver.get(link)

    project_title = get(".project_title h2 span")[0]
    
    if names[i] == project_title.text:
        score += 1

    time.sleep(2)

if score == 3:
    print_message("[+] Booth Setup Page is linked properly !!!")
else:
    raise TestFailed

driver.get("http://127.0.0.1:8080/general/student_dashboard_page/")
dashboard_controls_links = [a.get_attribute("href") for a in get(".dashboard-controls a")]

fr_page_link = dashboard_controls_links[0]
pr_page_link = dashboard_controls_links[1]

driver.get(fr_page_link)
time.sleep(2)
page_title = driver.title
if page_title == "Fest Registration Page":
    print_message("[+] Project Registration Page is linked properly !!!")
else:
    raise TestFailed

exit()

if page_title == "Project Registration Page":
    print_message("[+] Fest Registration Page is linked properly !!!")
else:
    raise TestFailed

input()
