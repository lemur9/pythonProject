import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chrome_options.binary_location = path

browser = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.baidu.com'
browser.get(url)

time.sleep(1)

input = browser.find_element(by='id', value='kw')
input.send_keys('周杰伦')
button = browser.find_element(by='id', value='su')
button.click()
time.sleep(1)
browser.save_screenshot('zhoujielun.png')

js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(1)

next = browser.find_element('xpath', '//a[@class="n"]')
next.click()


time.sleep(1)
browser.back()

time.sleep(1)

browser.forward()

time.sleep(1)

browser.quit()