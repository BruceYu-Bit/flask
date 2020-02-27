from selenium.webdriver import Chrome
import time
url = "http://www.baidu.com"

browser = Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe');
browser.get(url)

d1 = browser.find_element_by_xpath("//*[@id=\"u1\"]/a[8]")
d1.click()

time.sleep(1)


d2 = browser.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__footerULoginBtn\"]")
d2.click()
time.sleep(1)

in_id = browser.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__userName\"]")
in_id.send_keys("13856435512")
time.sleep(1)

in_pwd = browser.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__password\"]")
in_pwd.send_keys("164920wyy")
time.sleep(1)

browser.find_element_by_xpath("//*[@id=\"TANGRAM__PSP_10__submit\"]").click()





