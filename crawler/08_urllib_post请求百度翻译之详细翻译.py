from urllib import parse
from urllib import request as req
import json

url = 'https://fanyi.baidu.com/v2transapi?'

data = {
    "from": "en",
    "to": "zh",
    "query": "love",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "198772.518981",
    "token": "cc15502a1860cab5720807b110a93cea",
    "domain": "common"
}

headers = {
    'Cookie': 'BIDUPSID=BB41C4957F2E57FBE8EB4BF8364A0F30; PSTM=1680012419; BAIDUID=BB41C4957F2E57FB706F6F9E86F580DF:FG=1; BAIDUID_BFESS=BB41C4957F2E57FB706F6F9E86F580DF:FG=1; BAIDU_WISE_UID=wapp_1680415495572_8; ZFY=cLRPEAzip9tP0a:AOXAFLq7HEL6:ARv6C8WgS7avZaigI:C; delPer=0; PSINO=5; H_PS_PSSID=36548_38113_38470_38350_38359_38468_38289_38486_37938_26350_22159_37881; BDRCVFR[S4-dAuiWMmn]=FZ_Jfs2436CUAqWmykCULPYrWm1n1fz; BDUSS=WgxaFZjTXNLcGpkcjZhVH53R1pYLUlvYmlvUThhdjl3WUZZZlZiTHR2RlVjbFprSVFBQUFBJCQAAAAAAAAAAAEAAAAU2yjosKLA6s7Su9jIpQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTlLmRU5S5kb; BDUSS_BFESS=WgxaFZjTXNLcGpkcjZhVH53R1pYLUlvYmlvUThhdjl3WUZZZlZiTHR2RlVjbFprSVFBQUFBJCQAAAAAAAAAAAEAAAAU2yjosKLA6s7Su9jIpQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTlLmRU5S5kb; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1681137167; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1681137167; ab_sr=1.0.1_NGM3OWE4Y2FhNTRiMjFmZjQ5Mzc0MjI3ZGI3ODk4N2ZkNWIxMTE5YTFhY2IxYWI5ZWZkZDJmOGJiNjI3MDVmOWU3NWMzNzk2ZTM5MWE2YTVmMDYzNzZjNzUyOWYwZjY0YmIzNzRkODdkYjg4MTA3Yzc2YzUxY2UwMjA1ZWQ2ODNhN2U4ZTlhYThhOWEzODQ5NzA4ZWI3ZDY3Mzc1YmEzZjVjNTI2MTJmNTk4OGJmYjc5YTdhNzRhNzg0NWE5ODdi',
}

data = parse.urlencode(data).encode('utf-8')

request = req.Request(url=url, headers=headers, data=data)

response = req.urlopen(request)

content = response.read().decode('utf-8')

obj = json.loads(content)

print(obj)
