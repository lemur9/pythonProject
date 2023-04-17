from urllib import request as req

from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

response = req.urlopen(url)

content = response.read().decode('utf-8')
# print(content)

soup = BeautifulSoup(content, 'lxml')

name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    print(name.get_text())

# print(name_list)
