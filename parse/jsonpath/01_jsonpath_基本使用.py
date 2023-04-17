import json

import jsonpath

obj = json.load(open('jsonpath.json', 'r', encoding='utf-8'))

author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(author_list)

author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)
