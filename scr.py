#プラグインのインポートを行う
from typing import Text
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
#ヘッドレスモード(使用することにより、実際のサイトの表示はなくなる)
options.add_argument("--headless")
#シークレットモード
#options.add_argument("--incognito")


#driverを作成し、chromeを使用できるようにする
driver = webdriver.Chrome(
    executable_path = "/Users/kojimakentaro/Python-Scraping/chromedriver",options = options
)

#driver.getを使用し、サイトにアクセスを行う。(sleepを挟んで負荷をかけすぎないようにする。)
driver.get("https://www.yahoo.co.jp")
sleep(2)

i = driver.find_element_by_id("Topics")

print(i)
print(i.text)

#HTMLタグを指定して、そこにある情報を抽出する
#h2_tags = driver.find_elements_by_tag_name("h2")

#for h2_tag in h2_tags:
    #print(h2_tag.text)
    #print(h2_tag.get_attribute("outHTML"))


#要素から抜ける
driver.quit()





