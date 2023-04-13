from urllib import parse
from urllib import request as req
import json

url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'spider'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

data = parse.urlencode(data).encode('utf-8')

request = req.Request(url=url, headers=headers, data=data)

response = req.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)

