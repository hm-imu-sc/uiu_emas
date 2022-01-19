from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://127.0.0.1:8000/general/booth_setup_page/3/")
driver.maximize_window()

intro_video=driver.find_element_by_xpath('*[@id="intro_video"]')
Report=driver.find_element_by_xpath('*[@id="report"]')
demo_video=driver.find_element_by_xpath('*[@id="demo_videos"]')
intro_video.sendKeys("G:\Shamael/back up/23.12.21/user stuff/videos/1.mkv" )
Report.sendKeys("D:\Education\SAD\lab reatake\Pick-a-Book-Final-Report.pdf" )
#demo_video.sendKeys("G:\Shamael/back up/23.12.21\user stuff/videos/2.mkv" )

time.sleep(5)
submit = driver.find_element_by_xpath('/html/body/form/button')
submit.click()
driver.get("http://127.0.0.1:8000/cse_ps/project_booth_page/3/")
video = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/a[1]')
video.click()

print()