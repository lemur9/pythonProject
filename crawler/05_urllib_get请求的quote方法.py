from urllib import request as req
from urllib import parse

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

name = parse.quote('周杰伦')

url += name

request = req.Request(url=url, headers=headers)

response = req.urlopen(request)

content = response.read().decode('utf-8')

print(content)
