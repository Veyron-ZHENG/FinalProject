# -*- coding: utf-8 -*-

import json
import jieba

# # def loadData():

data = []

with open('items.json','r') as item_file:
    for line in item_file:
        data.append(json.loads(line))
l = jieba.cut(data[0]["review_body"])
l2 = jieba.cut(data[0]["review_body"],cut_all=True)
print ("/".join(l))
print "/".join(l2)
