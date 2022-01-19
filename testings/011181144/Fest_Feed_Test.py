from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:8000/")

time.sleep(1) 
driver.maximize_window()

time.sleep(1)

club_forum_fest_btn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/a[3]')
club_forum_fest_btn.click()
time.sleep(1) 

fest_feed_btn = driver.find_element_by_xpath('/html/body/div[4]/a[1]/i')
fest_feed_btn.click()
time.sleep(1) 

# Now in the fest feed page
# Test case [1]: Whether 5 posts are shown or not initially

post_len_span_1 = driver.find_element_by_xpath('//*[@id="posts_length"]') 
post_len_1 = post_len_span_1.get_attribute('length')

print("\nTest case [1]: Whether 5 posts are shown or not initially")
if int(post_len_1) == 5:
    print("Test Case 1 OK...!!!\n")
else:
    print("Test case 1 fails...!!!")
    print(f"Expected Length: 5 but found: {post_len_1}\n")

time.sleep(1) 
# Scroll Down till the end of that page
# driver.find_element_by_tag_name('html').send_keys(Keys.END)

total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")

time.sleep(1)

# Test case [2]: After clicking load more does the post length will be 10?

load_more_btn = driver.find_element_by_xpath('//*[@id="load-more"]')
load_more_btn.click()
time.sleep(1) 

# Again Scroll Down till the end of that page
# driver.find_element_by_tag_name('html').send_keys(Keys.END)
total_height2 = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(total_height+1, total_height2, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
time.sleep(2) 

post_len_span_2 = driver.find_element_by_xpath('//*[@id="posts_length"]') 
post_len_2 = post_len_span_2.get_attribute('length')

print("\nTest case [2]: After clicking load more does the post length will be 10?")
if int(post_len_2) == 10:
    print("Test Case 2 OK...!!!\n")
else:
    print("Test case 1 fails...!!!")
    print(f"Expected Length: 10 but found: {post_len_2}\n")

# time.sleep(1) 
# Scroll up[top] of the page
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

for i in range(total_height2, 1, -5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
# time.sleep(2)

time.sleep(2)

# Test case [3]: (Filtering) Posted by: "All" & Sort by: "Oldest"
# Expected Output: First Post will be "UIU Robotics Club" and Time will be: "Jan. 10, 2022, 9:03 p.m."

time.sleep(1) 
all_oldest = driver.find_element_by_xpath('//*[@id="sort_by"]/option[2]')
all_oldest.click()

time.sleep(1)       # Must
posted_by_name = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/h2/span[2]')
posted_by_time = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/h3/span[2]')

print("\nTest case [3]: (Filtering) Posted by: 'All' & Sort by: 'Oldest'")
if posted_by_name.text == "UIU Robotics Club" and posted_by_time.text == "Jan. 10, 2022, 9:03 p.m.":
    print("Test Case 3 OK...!!!\n")
else:
    print("Test case 3 failed...!!!")
    print("Expected Output--> Club Name: 'UIU Robotics Club' and Posted Time: 'Jan. 10, 2022, 9:03 p.m.'")
    print(f"But Found--> Club Name: {posted_by_name.text} and Posted Time: {posted_by_time.text}\n")

total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))
time.sleep(1)
# Scrolling UP in APP Forum Page
for i in range(total_height, 1, -5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

# Test case [4]: (Filtering) Posted by: "UIU APP Forum" & Sort by: "Oldest"
# Expected Output: First Post will be "UIU App Forum" and Time will be: "Jan. 10, 2022, 9:03 p.m."
time.sleep(1)
app_oldest = driver.find_element_by_xpath('//*[@id="club_name"]/option[3]')
app_oldest.click()

time.sleep(1)       # Must
posted_by_app = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/h2/span[2]')
posted_by_app_time = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/h3/span[2]')

print("\nTest case [4]: (Filtering) Posted by: 'UIU APP Forum' & Sort by: 'Oldest'")
if posted_by_app.text == "UIU App Forum" and posted_by_app_time.text == "Jan. 10, 2022, 9:03 p.m.":
    print("Test Case 4 OK...!!!\n")
else:
    print("Test case 4 failed...!!!")
    print("Expected Output--> Club Name: 'UIU App Forum' and Posted Time: 'Jan. 10, 2022, 9:03 p.m.'")
    print(f"But Found--> Club Name: {posted_by_app.text} and Posted Time: {posted_by_app_time.text}\n")

# Scrolling down in APP Forum Page
total_height = int(driver.execute_script("return document.body.scrollHeight"))

for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

# Scrolling UP in APP Forum Page
for i in range(total_height, 1, -5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

time.sleep(1)       

# Test case [5]: (Filtering) Posted by: "UIU APP Forum" & Sort by: "Newest"
# Expected Output: First Post will be "UIU App Forum" and Time will be: "Jan. 11, 2022, 3:39 p.m."

app_newest = driver.find_element_by_xpath('//*[@id="sort_by"]/option[1]')
app_newest.click()

time.sleep(1)       # Must
posted_by_app_new = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/h2/span[2]')
posted_by_app_time_new = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/h3/span[2]')

print("\nTest case [5]: (Filtering) Posted by: 'UIU APP Forum' & Sort by: 'Newest'")
if posted_by_app_new.text == "UIU App Forum" and posted_by_app_time_new.text == "Jan. 11, 2022, 3:39 p.m.":
    print("Test Case 5 OK...!!!\n")
else:
    print("Test case 5 failed...!!!")
    print("Expected Output--> Club Name: 'UIU App Forum' and Posted Time: 'Jan. 11, 2022, 3:39 p.m.'")
    print(f"But Found--> Club Name: {posted_by_app_new.text} and Posted Time: {posted_by_app_time_new.text}\n")


# Test case [6]: If no post available for a club
UIU_BC = driver.find_element_by_xpath('//*[@id="club_name"]/option[4]')
UIU_BC.click()

time.sleep(1)

post_card = driver.find_elements_by_class_name('post_card')

print('\nTest case [6]: If no post available for a club')
if len(post_card) == 0:
    print("Test Case 6 OK...!!!\n")
else:
    print("Test case 6 failed...!!!")
    print("Expected Output--> Number of posts should be 0")
    print(f"But Found--> Number of posts = {len(post_card)}\n")

# All & Newest
all_oldest = driver.find_element_by_xpath('//*[@id="club_name"]/option[1]')
all_oldest.click()

text = input()