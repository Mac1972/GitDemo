from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains  # 如果要輸入會員信箱&密碼要加這行
import time

#driver = webdriver.Chrome('D:\Program\chromedriver_win32\chromedriver.exe')  # 驅動程式路徑要設對
driver = webdriver.Chrome() # 趨動放進這個資料夾 C:\Users\Mac\AppData\Local\Programs\Python\Python37-32\Scripts
#driver = webdriver.Firefox() # 趨動放進這個資料夾 C:\Users\Mac\AppData\Local\Programs\Python\Python37-32\Scripts

driver.maximize_window()

#driver.fullscreen_window()

#driver.get('http://www.baidu.com')

#driver.get('http://www.douban.com')

#driver.get('http://www.google.com')

#driver.get('http://www.amazon.com')

#driver.get('http://www.timeanddate.com')

#driver.find_element_by_id('nav-your-amazon').click()

#driver.find_element_by_id('twotabsearchtextbox').send_keys('Mac')

#driver.find_element_by_name('q').send_keys('Mac\n') #  下一行 \n 代表將字輸入搜尋

#driver.find_element_by_link_text('Gmail').click()

#driver.find_element_by_class_name('lnk-movie').click()

#driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()

#driver.find_element_by_css_selector("#kw").send_keys('Mac\n')

#pageSource = driver.page_source

#print(pageSource)

#driver.back() #返回上頁

#driver.find_element_by_partial_link_text('mail').click()

#elements = driver.find_elements_by_tag_name('a')

#print(elements)

#for element in elements:
    #print(element)
    #print(element.text)
   #if '新闻' in  element.text:
       #element.click()



'''
selectElements = driver.find_element_by_id('month')
months = Select(selectElements)
months.select_by_visible_text('January')
countriesElements = driver.find_element_by_id('country')
counteries = Select(countriesElements)
counteries.select_by_visible_text('Taiwan')
driver.find_element_by_xpath("//div[4]//input[1]").click()
'''



#driver.find_element_by_name('q').send_keys('Mac\n')


driver.get("https://www.maccosmetics.com.tw/")

driver.find_element_by_class_name("first-name").click()
time.sleep(10)
driver.find_element_by_id("form--signin--field--EMAIL_ADDRESS").send_keys('xxx@xxx.com')
time.sleep(10)
driver.find_element_by_id("form--signin--field--PASSWORD").send_keys('xxxxxx')
time.sleep(10)
driver.find_element_by_css_selector("#signin > div.field-container > input").click()


#driver.save_screenshot('Google.png')

#driver.close()



#time.sleep(10)

#driver.quit()

