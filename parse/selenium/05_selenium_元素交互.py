import time
from selenium import webdriver

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

time.sleep(1)

input = browser.find_element(by='id', value='kw')
input.send_keys('周杰伦')
button = browser.find_element(by='id', value='su')
button.click()
time.sleep(1)
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(1)

next = browser.find_element('xpath', '//a[@class="n"]')
next.click()

time.sleep(1)
browser.back()

time.sleep(1)

browser.forward()

time.sleep(5)

browser.quit()