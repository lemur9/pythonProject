from urllib import request as req

url = 'https://www.jd.com/'

response = req.urlopen(url)

content = response.read().decode('utf-8')

print(content)