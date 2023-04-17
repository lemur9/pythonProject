import json
from urllib import request as req

import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1681561534496_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'referer': 'https://dianying.taobao.com/',
    'cookie': 't=e2737972d164176ed03c762313b9cc07; cookie2=12003079cbf7ed95a935c5cb308f77ca; v=0; _tb_token_=fe9d753717389; cna=wOCpHEEo5V8CAQAAAADU6ctq; xlly_s=1; tfstk=cwIOBxbYiWVgsmVDYhUngKl4tBSOZrNvOAOmDgmtW8lasHoAiujl2AM35KOy6JC..; l=fBIdilauNIKLa3X3BO5aourza77tZIdb8sPzaNbMiIEGa61hTFMAKNCs7MgD7dtjgTfceetr24w81dHw5wUKggiMW_N-1NKDFYp6-bpU-L5..; isg=BOXl1IkO7d7EOAkCwNJ0qn-O9KEfIpm0usc-LufLbZwr_gRwr3DMhClYiGKIfrFs',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

request = req.Request(url=url, headers=headers)

response = req.urlopen(request)

content = response.read().decode('utf-8')

content = content.split('(')[1].split(')')[0]

with open('jsonpath解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('jsonpath解析淘票票.json', 'r', encoding='utf-8'))

obj = jsonpath.jsonpath(obj, '$..regionName')
print(obj)
