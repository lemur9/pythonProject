import json
from urllib import request as req

headers = {
    # 'accept': 'application/json, text/plain, */*',
    # 'accept-language': 'zh-CN,zh;q=0.9',
    # 'cache-control': 'no-cache',
    'cookie': '_T_WM=92138524632; WEIBOCN_FROM=1110006030; SCF=AivzlUYtxlT_am8y8a5JV7KYzaDxXwyBvD1xIfPuUPpUzv1-UFyMLHUWRuU1yiAvzMhHiFzWkRFN2E8Dxv3nKXw.; SUB=_2A25JPLi7DeRhGeFG6FEQ8i7KzjiIHXVq3tjzrDV6PUJbktANLUrykW1NedOsKlTx8Lw8pvmLJnJxTwFJxA-GAhkf; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF_889ofcxITjEFNKMNwciU5JpX5K-hUgL.FoMRe0epeo5cSKB2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1he0eKz7So-X; SSOLoginState=1681443051; WEIBOCN_WM=3349; MLOGIN=1; XSRF-TOKEN=6ef2aa; mweibo_short_token=941acec6b4; M_WEIBOCN_PARAMS=oid%3D4890369885732971%26luicode%3D10000011%26lfid%3D102803%26uicode%3D20000174',
    # 'mweibo-pwa': 1,
    # 'pragma': 'no-cache',
    'referer': 'https://m.weibo.cn/',
    # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': "Windows",
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 'x-requested-with': 'XMLHttpRequest',
    # 'x-xsrf-token': '6ef2aa',
}
url = 'https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0'

request = req.Request(url=url, headers=headers)
response = req.urlopen(request)
content = response.read().decode('utf-8')

obj = json.loads(content)
obj = json.dumps(obj=obj, ensure_ascii=False)

with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(obj)
