import os
import pickle
from selenium import webdriver
from bs4 import BeautifulSoup


cookieFile = "cookie.pkl"
cookies = None

if os.path.exists(cookieFile):
    with open(cookieFile, "rb") as inFile: cookies = pickle.load(inFile)

driver = webdriver.Firefox()
if cookies is not None:
    driver.get("https://weibo.com")
    for co in cookies: driver.add_cookie(co)
driver.get("https://weibo.com")
_ = input("press ENTER after login to weibo")


# 跳转到搜索“腾讯”官方号
driver.get(r"https://s.weibo.com/user?q=%E8%85%BE%E8%AE%AF&auth=org_vip&page=1")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())


_ = input("press ENTER to close")


driver.get("https://weibo.com")
with open(cookieFile, "wb") as outFile:
    pickle.dump(driver.get_cookies(), outFile)

driver.close()