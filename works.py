from typing import Text
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--headless")


#driverを作成し、chromeを使用できるようにする
driver = webdriver.Chrome(
    executable_path = "/Users/kojimakentaro/Python-Scraping/chromedriver",options = options
)
driver.implicitly_wait(10)


#driver.getを使用し、サイトにアクセスを行う。(sleepを挟んで負荷をかけすぎないようにする。)
driver.get("https://atsumaru.jp/area/7/list?sagid=all")
sleep(2)

height = driver.execute_script("return document.body.scrollHeight")
new_height = 0

while True:
    print(height)
    driver.execute_script(f"window.scrollTo(0,{height})")
    sleep(3)

    new_height = driver.execute_script("return document.body.scrollHeight")

    if height == new_height:
        break

    height = new_height

with open("company_list.html" ,  "w")as f:
    f.write(driver.page_source)

driver.quit()

