import requests
from urllib import request
from bs4 import BeautifulSoup
from selenium import webdriver
import re

url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/2020/2/26/790337e913cd41f0b71938fe7ca2ae75.shtml"
res = requests.get(url)
res.encoding = "utf-8"

html = res.text

regex = "新增确诊病例(\d+)例"

confirmadd = re.search(regex,html)
print(confirmadd)
print(confirmadd.groups())
print(confirmadd.group(0))

browser = webdriver.Chrome(executable_path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('http://www.baidu.com')