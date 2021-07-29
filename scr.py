#プラグインのインポートを行う
from typing import Text
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os


options = webdriver.ChromeOptions()
#ヘッドレスモード(使用することにより、実際のサイトの表示はなくなる)
options.add_argument("--headless")
#シークレットモード
#options.add_argument("--incognito")


#driverを作成し、chromeを使用できるようにする
driver = webdriver.Chrome(
    executable_path = "/Users/kojimakentaro/Python-Scraping/chromedriver",options = options
)
driver.implicitly_wait(10)


#driver.getを使用し、サイトにアクセスを行う。(sleepを挟んで負荷をかけすぎないようにする。)
driver.get("https://www.yahoo.co.jp")
sleep(2)


#スクロール作業を行う
#height = driver.execute_script("return document.body.scrollHeight")
#sleep(3)
#driver.execute_script(f"window.scrollTo(0,{height})") #(x,y")で記入を行う
#sleep(3)


#クラスやidを検証を使用してサイトから取得する
#a = driver.find_element_by_class_name("_2jjSS8r_I9Zd6O9NFJtDN-")
#i = driver.find_element_by_id("Topics")

#print(a)
#print(a.text)
"""
#検索タブに関しての操作(文字を入力を行う)
search_box = driver.find_element_by_css_selector("input.nxrKmn7Pk9iZExZ0kdJ4Z")
sleep(2)
search_box.send_keys("オリンピック")
sleep(5)
#実際に検索ボタンを押す
search_box.submit()
sleep(3)

#最下点まで移動する
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(2)

    #次のページのボタンを押す
    a = driver.find_elements_by_css_selector("div.Contents__inner.Co > div > div > div > div > a")
    sleep(3)

    #ページ移動のボタンを押す
    if a:
        a[0].click()
    else:
        break
#スクロール作業を行う
#height = driver.execute_script("return document.body.scrollHeight")
#sleep(3)
#driver.execute_script(f"window.scrollTo(0,{height})") #(x,y")で記入を行う
#sleep(3)


#HTMLタグを指定して、そこにある情報を抽出する
#h2_tags = driver.find_elements_by_tag_name("h2")

#for h2_tag in h2_tags:
    #print(h2_tag.text)
#サイトのurlも取得したい場合のコード
    #print(h2_tag.get_attribute("href"))
    #print(h2_tag.get_attribute("outHTML"))


#seleniumで各URLにアクセスして、ページのHTMLを取得する
dir_name = os.path.dirname(os.path.abspath(__file__))
for i,url in enumerate(url):
    print("="*30, i,"="*30)
    print(url)
    driver.get(url)
    sleep(5)

    html = driver.page_source

    #p = f"/Users/kojimakentaro/Python-Scraping/html/{driver.title}.html"
    p = os.path.join(dir_name,"html",f"{driver.title}.html")

    with open(p,"w") as f:
        f.write(html)


"""
#要素から抜ける
driver.quit()





