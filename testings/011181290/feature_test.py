
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By as by
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.common.exceptions import StaleElementReferenceException

root = "http://127.0.0.1:8000"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(root)

class TestFailed(Exception):
    pass

def sleep_for(sec):
    time.sleep(sec)

def print_message(str):
    print(f"\n\n{str}\n\n")

def get(css_selector, element=None):
    if element is not None:
        return element.find_elements(by.CSS_SELECTOR, css_selector)
    return driver.find_elements(by.CSS_SELECTOR, css_selector)

login_page_link = get(".utility-item .nav-item:nth-child(2)")[0]

login_page_link.click()
sleep_for(2)

u_email = "hbillah181290@bscse.uiu.ac.bd"
u_password = "password"

uname_field = get("#user")[0]
uname_field.send_keys(u_email)

pass_field = get("#password")[0]
pass_field.send_keys(u_password)
sleep_for(2)

login_btn = get("input[type=\"submit\"]")[0]
login_btn.click()

page_title = driver.title

if page_title == "student Dashboard":
    print_message("[+] Login Test Successfull !!!")
else:
    raise TestFailed
sleep_for(2)

appr_proj_btn = get("#appr_proj")[0]
appr_pen_proj_btn = get("#appr_pen_proj")[0]

appr_pen_proj_btn.click()
sleep_for(2)

projects = get(".project")
if len(projects) == 1:
    print_message("[+] Approval pending projects tab is working properly !!!")
else:
    raise TestFailed

appr_proj_btn.click()
sleep_for(2)

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

    sleep_for(2)

if score == 3:
    print_message("[+] Booth Setup Page is linked properly !!!")
else:
    raise TestFailed

driver.get(f"{root}/general/student_dashboard_page/")
dashboard_controls_links = [a.get_attribute("href") for a in get(".dashboard-controls a")]

fr_page_link = dashboard_controls_links[0]
pr_page_link = dashboard_controls_links[1]

driver.get(fr_page_link)
sleep_for(2)
page_title = driver.title
if page_title == "Fest Registration Page":
    print_message("[+] Project Registration Page is linked properly !!!")
else:
    raise TestFailed

driver.get(pr_page_link)
sleep_for(2)
page_title = driver.title
if page_title == "Project Registration Page":
    print_message("[+] Fest Registration Page is linked properly !!!")
else:
    raise TestFailed

driver.get(f"{root}/cse_ps/index/")
sleep_for(2)

project_booths_link = get(".options a:nth-child(1)")[0]
project_booths_link.click()
sleep_for(2)

courses = get(".courses a")

if len(courses) == 3:
    print_message("[+] Course list is showing properly !!!")
else:
    raise TestFailed

courses[1].click()
sleep_for(2)

project_booths = get(".booth_thumbnail")

if len(project_booths) == 6:
    print_message("[+] Project booth list is loading properly !!!")
else:
    raise TestFailed

project_name = get(".project_name span:nth-child(2)", project_booths[0])[0].text

project_booth = get("a", project_booths[0])[0]
project_booth.click()
sleep_for(2)

project_name_after = get("h1.title")[0].text

if project_name == project_name_after:
    print_message("[+] Project booth is loaded properly !!!")
else:
    raise TestFailed

comment_length = int(get("#comment-length")[0].get_attribute("length"))

comment_box = get("#new-comment")[0]
comment_box.send_keys("this comment is sent using send button")
sleep_for(2)

send_btn = get("#comment-send-btn")[0]
send_btn.click()

comment_box.clear()
comment_box.send_keys("this comment is sent by pressing enter")
sleep_for(2)

comment_box.send_keys(Keys.RETURN)

sleep_for(2)

new_comment_length = int(get("#comment-length")[0].get_attribute("length"))

if new_comment_length == comment_length + 2:
    print_message("[+] Send comment is working properly by both Enter key press and Send button !!!")

input()
