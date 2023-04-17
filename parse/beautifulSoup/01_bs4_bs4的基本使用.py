from bs4 import BeautifulSoup

soup = BeautifulSoup(open('bs4的基本使用.html', 'r', encoding='utf-8'), 'lxml')

# print(soup.a)
# print(soup.a.attrs)

# print(soup.find('a', title='a2'))
print(soup.find('a', class_='a1'))
# print(soup.find_all('a'))
print(soup.find_all('li', limit=2))

print(soup.find_all(['a', 'span']))
print(soup.select('a'))

print(soup.select('.a1'))
print(soup.select('#l1'))

print(soup.select('li[id]'))
print(soup.select('li[id="l2"]'))

print(soup.select('div li'))

print(soup.select('div > ul > li'))

print(soup.select('a,li'))
