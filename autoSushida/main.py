
# python main.py
from selenium import webdriver

# ドライバーを開く
driver = webdriver.Chrome()

# ウィンドウサイズを指定
window = (500, 420 + 123)
driver.set_window_size(*window)

target_url = "https://sushida.net/"
driver.get(target_url)

# ゲーム画面をずらすための記載
target_xpath = '//*[@id="game"]/div'
webgl_element = driver.find_element_by_xpath(target_xpath)
actions = ActionChains(driver)
actions.move_to_element(webgl_element).perform()

input("何か入力してください")

# ドライバーを閉じる
driver.close()
driver.quit() # ターミナルでEnterで閉じる
