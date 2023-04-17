from urllib import request as req

from lxml import etree


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/katongtupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/katongtupian_' + str(page) + '.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    return req.Request(url=url, headers=headers)


def get_content(request):
    response = req.urlopen(request)
    return response.read().decode('utf-8')


def dowm_load(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="item"]/img/@alt')
    src_list = tree.xpath('//div[@class="item"]/img/@data-original')
    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        url = "https:" + src
        req.urlretrieve(url=url, filename='./img/' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输入终止页码'))
    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        dowm_load(content)
