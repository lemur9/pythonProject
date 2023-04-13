from urllib import request

url = "http://www.baidu.com"

response = request.urlopen(url)

print(type(response))

print(response.getcode())

print(response.geturl())

print(response.getheaders())

#一个类型   HTTPResponse
#六个方法   read readline readlines getcode geturl getheaders

