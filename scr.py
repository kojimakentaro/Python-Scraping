#プラグインのインポートを行う
from typing import Text
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
#ヘッドレスモード(使用することにより、実際のサイトの表示はなくなる)
#options.add_argument("--headless")
#シークレットモード
#options.add_argument("--incognito")


#driverを作成し、chromeを使用できるようにする
driver = webdriver.Chrome(
    executable_path = "/Users/kojimakentaro/Python-Scraping/chromedriver",options = options
)
driver.implicitly_wait(10)


#driver.getを使用し、サイトにアクセスを行う。(sleepを挟んで負荷をかけすぎないようにする。)
driver.get("https://www.google.com")
sleep(2)

#サイトまでたどり、クリック検索を行う
#a_tag = driver.find_element_by_css_selector("div._2jjSS8r_I9Zd6O9NFJtD > ul > li:nth-of-type(2) > a")
#sleep(3)

#a_tag.click()
#sleep(3)


#クラスやidを検証を使用してサイトから取得する
#a = driver.find_element_by_class_name("_2jjSS8r_I9Zd6O9NFJtDN-")
#i = driver.find_element_by_id("Topics")

#print(a)
#print(a.text)

#検索タブに関しての操作(文字を入力を行う)
#search_box = driver.find_element_by_css_selector("input.nxrKmn7Pk9iZExZ0kdJ4Z")
#sleep(2)
#search_box.send_keys("オリンピック")
#sleep(5)
#実際に検索ボタンを押す
#search_box.submit()



#HTMLタグを指定して、そこにある情報を抽出する
#h2_tags = driver.find_elements_by_tag_name("h2")

#for h2_tag in h2_tags:
    #print(h2_tag.text)
#サイトのurlも取得したい場合のコード
    #print(h2_tag.get_attribute("href"))
    #print(h2_tag.get_attribute("outHTML"))


#要素から抜ける
driver.quit()





