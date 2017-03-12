# -*- coding: utf-8 -*-

import jieba.posseg as pseg
import jieba
import jieba.analyse
import json

jieba.load_userdict("features_dict.txt")
jieba.analyse.set_stop_words('stopwords.txt')

# jieba.suggest_freq("很帅",True)
file_to_store = open("reviews_tagged.txt","w")
with open("reviews_cutted.txt","r") as file:
    for line in file:
        if line == "\n":
            continue
        line_list = line.strip().split(",")
        word_flag_dict = {}
        for word in line_list:
            word_flag = pseg.cut(word)
            for w,f in word_flag:
                word_flag_dict[w]=f
        data = json.dumps(word_flag_dict)
        file_to_store.write(data)
file_to_store.close()