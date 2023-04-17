from urllib import request as req

url = 'http://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

request = req.Request(url=url, headers=headers)

# 1)获取handler对象
handler = req.HTTPHandler()

# 2)获取opener对象
opener = req.build_opener(handler)

# 3)调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

print(content)