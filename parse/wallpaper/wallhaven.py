from urllib import request as req

from lxml import etree


def create_request(page):
    url = 'https://wallhaven.cc/search?categories=111&purity=100&sorting=relevance&order=desc&ai_art_filter=1'
    if page != 1:
        url = url + '&page=' + str(page)

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    return req.Request(url=url, headers=headers)


def get_content(request):
    response = req.urlopen(request)
    return response.read().decode('utf-8')


def dowm_load(content):
    print(content)
    tree = etree.HTML(content)
    src_list = tree.xpath('//div[@id="thumbs"]/section/ul/li/figure/img/@data-src')
    for i in range(len(src_list)):
        src = src_list[i]
        name = str(src).split('/')[-1]

        opener = req.build_opener()
        opener.addheaders = [('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36')]
        req.install_opener(opener)

        req.urlretrieve(url=src, filename='./img/' + name)
        print(name, src)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入终止页码'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        dowm_load(content)
