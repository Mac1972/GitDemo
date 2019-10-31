from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains  # 如果要輸入會員信箱&密碼要加這行
import time

#driver = webdriver.Chrome('D:\Program\chromedriver_win32\chromedriver.exe')  # 驅動程式路徑要設對
driver = webdriver.Chrome() # 趨動放進這個資料夾 C:\Users\Mac\AppData\Local\Programs\Python\Python37-32\Scripts
#driver = webdriver.Firefox() # 趨動放進這個資料夾 C:\Users\Mac\AppData\Local\Programs\Python\Python37-32\Scripts

driver.maximize_window()

driver.get("https://www.google.com/")

driver.find_element_by_css_selector("#gb_70").click()
time.sleep(10)
driver.find_element_by_css_selector("#identifierId").send_keys('xxx@xxx.com')
#time.sleep(10)
#driver.find_element_by_id("form--signin--field--PASSWORD").send_keys('xxxxxx')
#time.sleep(10)
#driver.find_element_by_css_selector("#signin > div.field-container > input").click()