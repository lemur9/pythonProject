import random
from urllib import request as req

proxies_pool = [
    # {'http': '182.139.110.36:9000'},
    # {'http': '113.121.36.199:9999'},
    # {'http': '61.216.185.88:60808'},
    # {'http': '123.169.39.212:9999'},
    {'http': '64.233.189.188:5228'},
]

proxy = random.choice(proxies_pool)
print(proxy)

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'Referer': 'https://www.baidu.com/s?wd=ip',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

request = req.Request(url=url, headers=headers)

handler = req.ProxyHandler(proxies=proxy)

opener = req.build_opener(handler)
response = opener.open(request)
content = response.read().decode('utf-8')

print(content)
