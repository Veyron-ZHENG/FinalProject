# -*- coding: utf-8 -*-

import jieba.posseg as pseg
import jieba
import jieba.analyse
import json

# jieba.load_userdict("features_dict.txt")
# jieba.analyse.set_stop_words('stopwords.txt')
#
# with open('reviews.txt','r') as file:
#     for line in file:
#         tags = jieba.analyse.extract_tags(line,topK=10)
#         print ','.join(tags)
#

# def position_gen(maxi):
#     sign = -1
#     for i in range(1,maxi+1):
#         for j in range(2):
#             yield sign*i
#             sign = (-1)*sign
#
# a = position_gen(4)
#
# for i in a:
#     print i
#
# b = range(4)
# b.reverse()
# print b

with open('sentiment/positive.txt','r') as file:
    for line in file:
        print line.strip()