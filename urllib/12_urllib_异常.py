from urllib import request as req
from urllib import error as err

url = 'https://blog.csdn.net/sulixu/article/details/119818949'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
}

try:
    request = req.Request(url=url, headers=headers)

    response = req.urlopen(url)

    content = response.read().decode('utf-8')

    print(content)
except err.HTTPError:
    print("出现错误")
