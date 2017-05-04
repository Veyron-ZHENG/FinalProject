# -*- coding: utf-8 -*-

import jieba.posseg as pseg
import jieba
import jieba.analyse
import json

jieba.load_userdict("features_dict.txt")
jieba.analyse.set_stop_words('stopwords.txt')

with open('reviews.txt','r') as file:
    for line in file:
        tags = jieba.analyse.extract_tags(line,topK=10)
        print ','.join(tags)