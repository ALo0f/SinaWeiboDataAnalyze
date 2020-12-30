import os
import pickle
import pandas as pd
from selenium import webdriver


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


sina = pd.read_csv("sina.csv")
to_remove = []
for i, row in sina.iterrows():
    print(row["名字"])
    driver.get(row["url"])
    a = input("is this valid account? Y/N")
    while a.upper() not in ["Y", "N"]:
        a = input("is this valid account? Y/N")
    if a.upper() == "N":
        to_remove.append(i)
with open("tmp.pkl", "wb") as outFile:
    pickle.dump(to_remove, outFile)
new_sina = sina.drop(sina.index[to_remove])
new_sina.reset_index(inplace=True, drop=True)
new_sina.to_csv("processed4basics.csv", encoding="utf-8-sig", index=False)

_ = input("press ENTER to close")


driver.get("https://weibo.com")
with open(cookieFile, "wb") as outFile:
    pickle.dump(driver.get_cookies(), outFile)

driver.close()