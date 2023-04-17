from urllib import request as req

from lxml import etree

url = 'http://www.baidu.com/'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

request = req.Request(url=url, headers=headers)

response = req.urlopen(request)
content = response.read().decode("utf-8")

tree = etree.HTML(content)

result = tree.xpath("//input[@id='su']/@value")[0]
print(result)
