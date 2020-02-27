import requests
from urllib import request
from bs4 import BeautifulSoup
# r = requests.get('http://www.kaoyan.com/daoshi/')
# print(r.text)

# url = "http://www.baidu.com"
# res = request.urlopen(url)
#
# print(res.geturl())
# print(res.getcode())
# print(res.info())
#
# html = res.read();
# html = html.decode("utf-8") #解码
# print(html)


#加头
# url2= "http://www.dianping.com"
# header = {
#     "Host": "www.dianping.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# }
#
# res2 = request.Request(url=url2,headers=header)
# res3 = request.urlopen(res2)
# print(res3.getcode())

#第三种
# url2= "http://www.dianping.com"
# header = {
#     "Host": "www.dianping.com",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
# }
# res = requests.get(url2,headers=header)
# print(res.status_code)
# print(res.encoding)
# #上下文管理器
# with open("daanping.txt","w",encoding="utf-8") as f:
#     f.write(res.text)
#
# html = res.text
# #beautifulsoup
# soup = BeautifulSoup(html)
# a = soup.select("#cata-hot > div > ul > li.hot-item > a")
# print(type(a),len(a))
# print(a[0].attrs.get("href"),a[0].text)
#
# for i in a:
#     print(i.attrs.get("href"),i.text)