
# python main.py
from selenium import webdriver

# ドライバーを開く
driver = webdriver.Chrome()

target_url = "https://sushida.net/"
driver.get(target_url)

input("何か入力してください")

# ドライバーを閉じる
driver.close()
