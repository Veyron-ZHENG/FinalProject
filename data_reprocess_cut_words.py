# -*- coding: utf-8 -*-

import jieba
import jieba.analyse
# import nltk.FreqDist
import nltk

data = []
with open("reviews.txt","r") as file:
    for line in file:
        data.append(line)

jieba.load_userdict("features_dict.txt")
jieba.analyse.set_stop_words('stopwords.txt')

with open("reviews_cutted.txt","w") as file:
    for review in data:
        words = list(jieba.cut(review))
        word_list = []
        for word in words:
            word_list += jieba.analyse.extract_tags(word)
        word_list = map(lambda x: x.encode("utf-8"),word_list)
        file.write(",".join(word_list))
        file.write("\n")

    # f = nltk.FreqDist(review_words_cutted)
    # for key in f.keys():
    #     print key+" "+str(f.get(key))
    # print "/".join(f.keys())
    # print f.get("质量".decode("utf-8"))
    # print f.get("很好".decode("utf-8"))
    # for key in f.keys():
    #     print key+"    "+str(f[key])