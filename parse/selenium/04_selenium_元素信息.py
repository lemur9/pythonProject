from selenium import webdriver

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

input = browser.find_element(by='id', value='su')

print(input.get_attribute('class'))
print(input.tag_name)
print(input.text)

a = browser.find_element(by='link text', value='新闻')
print(a.text)
