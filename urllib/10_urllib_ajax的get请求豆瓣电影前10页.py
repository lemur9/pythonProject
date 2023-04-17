import json
from urllib import parse
from urllib import request as req

base_url = "https://m.douban.com/rexxar/api/v2/movie/suggestion?"

headers = {
    'Referer': 'https://m.douban.com/movie/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}


def create_request(page):
    data = {
        'start': (page - 1) * 10,
        'count': 10,
        'new_struct': 1,
        'with_review': 1,
        'for_mobile': 1
    }
    data = parse.urlencode(data)
    url = base_url + data

    print(url)

    return req.Request(url=url, headers=headers)


def get_content(request):
    response = req.urlopen(request)
    return response.read().decode("utf-8")


def down_load(page, content):
    obj = json.loads(content)
    obj = json.dumps(obj=obj, ensure_ascii=False)
    with open('.//douban//douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(obj)


if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码')) + 1

    for page in range(start_page, end_page):
        request = create_request(page)
        content = get_content(request)
        down_load(page, content)
