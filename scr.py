#プラグインのインポートを行う
from typing import Text
import requests
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
#ヘッドレスモード(使用することにより、実際のサイトの表示はなくなる)
#options.add_argument("--headless")
#シークレットモード
options.add_argument("--incognito")


#driverを作成し、chromeを使用できるようにする
driver = webdriver.Chrome(
    executable_path = "/Users/kojimakentaro/Python-Scraping/chromedriver",options = options
)

#driver.getを使用し、サイトにアクセスを行う。(sleepを挟んで負荷をかけすぎないようにする。)
driver.get("https://www.google.co.jp")
sleep(2)

#要素から抜ける
driver.quit()





