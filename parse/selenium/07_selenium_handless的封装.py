import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser(chrome_path):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    path = chrome_path
    chrome_options.binary_location = path

    browser = webdriver.Chrome(chrome_options=chrome_options)
    return browser

browser = share_browser('C:\Program Files\Google\Chrome\Application\chrome.exe')

url = 'https://www.baidu.com'

browser.get(url)
browser.save_screenshot('baidu.png')
browser.quit()