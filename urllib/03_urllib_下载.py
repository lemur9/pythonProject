from urllib import request

url = "http://www.baidu.com"

response = request.urlretrieve(url, 'baidu.html')
