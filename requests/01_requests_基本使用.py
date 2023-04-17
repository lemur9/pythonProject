import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

response.encoding='utf-8'

print(response.text)

print(response.url)

print(response.content)

print(response.status_code)

print(response.headers)