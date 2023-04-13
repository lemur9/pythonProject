from urllib import request as req
from urllib import parse
import json

base_url = 'https://m.douban.com/rexxar/api/v2/movie/suggestion?'

data = {
    'start': '0',
    'count': '10',
    'new_struct': '1',
    'with_review': '1',
    'for_mobile': '1'
}

data = parse.urlencode(data)

url = base_url + data

headers = {
    'Referer': 'https://m.douban.com/movie/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

request = req.Request(url=url, headers=headers)

response = req.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)
obj = json.dumps(obj=obj, ensure_ascii=False)

print(obj)

with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(obj)
