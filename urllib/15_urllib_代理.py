from urllib import request as req

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'Referer': 'https://www.baidu.com/s?wd=ip',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

request = req.Request(url=url, headers=headers)

# response = req.urlopen(request)

proxies = {
    'http': '123.169.39.212:9999'
}

handler = req.ProxyHandler(proxies=proxies)

opener = req.build_opener(handler)

response = opener.open(request)

content = response.read().decode('utf-8')

with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
