#常规手段赚不到数据js渲染
import requests
from selenium.webdriver import Chrome,ChromeOptions
import time
option = ChromeOptions()
option.add_argument('--headless') #在后台启动
url = "https://voice.baidu.com/act/virussearch/virussearch?from=osai_map&tab=0&infomore=1"
res =requests.get(url)
# print(res.status_code)
# print(res.encoding)
# print(res.text)

browser = Chrome(options=option,executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get(url)
html = browser.page_source

a = browser.find_element_by_class_name('VirusHot_1-4-9_1Fqxy-')
a.click()
time.sleep(2)

all_a = browser.find_elements_by_css_selector('.VirusHot_1-4-9_2RnRvg > section > a')
for i in all_a:
   print(i.text,i.get_attribute('href'))


#模拟点击


#browser.get(new_url) #打开新的连接



browser.close()

