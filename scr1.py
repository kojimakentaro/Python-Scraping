from time import sleep, time
import requests
from bs4 import BeautifulSoup
import pandas as pd

#urlを取得する
url = ""
r = requests.get(url,timeout = 3)
r.raise_for_status()
soup = BeautifulSoup(r.content,"xlml")

#会社情報を取得する
companies = soup.find_all("div",class_ = "")

d_list = []
for company in companies:
    #企業名を取得
    company_name = company.find("span",class_ = "company").text
    #URLを取得
    page_url = company.find("a",class_ = "").get("href")
    #必要なURLにタブを変更する
    page_url = page_url.replace("-tab_pr","-tab_id")

    sleep(3)

    page_r = requests.get(page_url,timeout = 3)
    page_r.raise_for_status()

    page_soup = BeautifulSoup(page_r.content,"lxml")

    table = page_soup.find("table",id = "company_prifile_table")
    company_url = table.find("a").get("href")

    d_list.append({
        "company_name":company_name,
        "company_url":company_url
    })

#csvで保存
df = pd.DataFrame(d_list)
df.to_csv("company.csv",index=None,encoding="utf-8-sig")