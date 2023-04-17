from urllib import parse
from urllib import request as req

# http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname

# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
}


def create_request(page):
    data = {
        "cname": "北京",
        "pid": "",
        "pageIndex": int(page),
        "pageSize": 10,
    }
    print(data)
    data = parse.urlencode(data).encode("utf-8")
    return req.Request(url=base_url, headers=headers, data=data)


def get_content(request):
    response = req.urlopen(request)
    return response.read().decode("utf-8")


def down_load(page, content):
    with open(".//kfc//kfc_addr" + str(page) + ".json", "w", encoding="utf-8") as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码')) + 1

    for page in range(start_page, end_page):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)
