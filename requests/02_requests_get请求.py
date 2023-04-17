import requests

url = 'https://www.baidu.com/s'

headers = {
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Cache-Control': 'no-cache',
    # 'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=BB41C4957F2E57FBE8EB4BF8364A0F30; PSTM=1680012419; BAIDUID=BB41C4957F2E57FB706F6F9E86F580DF:FG=1; BD_UPN=12314753; BAIDUID_BFESS=BB41C4957F2E57FB706F6F9E86F580DF:FG=1; BAIDU_WISE_UID=wapp_1680415495572_8; ZFY=cLRPEAzip9tP0a:AOXAFLq7HEL6:ARv6C8WgS7avZaigI:C; channel=google; Hm_lvt_aec699bb6442ba076c8981c6dc490771=1680416190; baikeVisitId=88e9abdb-3187-4fe7-9253-d414a405ebec; COOKIE_SESSION=1685_0_9_9_2_18_0_0_9_8_3_2_15_0_0_0_1680355820_0_1680417477%7C9%230_0_1680417477%7C1; delPer=0; BD_CK_SAM=1; PSINO=5; BDRCVFR[S4-dAuiWMmn]=FZ_Jfs2436CUAqWmykCULPYrWm1n1fz; BD_HOME=1; BDUSS=WgxaFZjTXNLcGpkcjZhVH53R1pYLUlvYmlvUThhdjl3WUZZZlZiTHR2RlVjbFprSVFBQUFBJCQAAAAAAAAAAAEAAAAU2yjosKLA6s7Su9jIpQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTlLmRU5S5kb; BDUSS_BFESS=WgxaFZjTXNLcGpkcjZhVH53R1pYLUlvYmlvUThhdjl3WUZZZlZiTHR2RlVjbFprSVFBQUFBJCQAAAAAAAAAAAEAAAAU2yjosKLA6s7Su9jIpQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFTlLmRU5S5kb; H_PS_PSSID=38515_36548_38470_38350_38359_38468_38485_37938_37709_38506_26350_22159; BA_HECTOR=00040l01218g2521240h0l4n1i3muii1m; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDSVRTM=9; WWW_ST=1681619557635',
    # 'Host': 'www.baidu.com',
    # 'is_referer': 'https://www.baidu.com/',
    # 'is_xhr': '1',
    # 'Pragma': 'no-cache',
    # 'Ps-Dataurlconfigqid': '0x9e79fd540020faec',
    # 'Referer': 'https://www.baidu.com/s?',
    # 'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
}

data = {
    'wd': '北京'
}

response = requests.get(url=url, params=data, headers=headers)
response.encoding = 'utf-8'
print(response.text)
