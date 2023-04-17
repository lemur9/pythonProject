from selenium import webdriver

path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'
browser.get(url)

# button = browser.find_element_by_id('su')
# button = browser.find_element_by_name('wd')
# button = browser.find_elements_by_tag_name('input')
# button = browser.find_elements_by_css_selector('#su')
# button = browser.find_elements(by='xpath', value='//input[@id="su"]')
# button = browser.find_elements_by_link_text('新闻')
"""
    统一了，用法如下
"""
button = browser.find_elements(by='link text', value='新闻')

print(button)
