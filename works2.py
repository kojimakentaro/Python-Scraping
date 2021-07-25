from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from urllib3 import request
from typing import Text
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

with open("company_list.html" ,  "r")as f:
    html = f.read()

soup = BeautifulSoup(html,"lxml")

a_tags = soup.select("span.exe > a")

d_list = []

for i,a_tag in enumerate(a_tags):
    url = "https://atsumaru.jp/" + a_tag.get("href")

    r = requests.get(url)
    r.raise_for_status()

    sleep(3)

    page_soup = BeautifulSoup(r.content,"lxml")
    
    company_name = page_soup.select_one("#detailBox > h2").text
    tel = page_soup.select_one("div.telNo > p> strong > a").text

    d_list.append({
        "company_name":company_name,
        "tel":tel

    })
    print("="*30,i,"="*30)
    print(d_list[-1])

    if i > 10:
        break

df = pd.DataFrame(d_list)
df.to_csv("company_list.csv",index = None,encoding="utf-8-sig")