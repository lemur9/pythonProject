from urllib import request

url = "http://www.baidu.com"

response = request.urlopen(url)

content = response.read().decode("utf-8")

print(content)
