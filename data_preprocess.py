# -*- coding: utf-8 -*-

import jieba.posseg as pseg
import jieba
import jieba.analyse
import json



jieba.load_userdict("features_dict.txt")
jieba.analyse.set_stop_words('stopwords.txt')

file_to_store = open('data_outcome/data_preprocessed.json','w')

with open("reviews.txt","r") as file:
    for line in file:
        word_flage_dict={}
        word_flage = pseg.cut(line)
        for w, f in word_flage:
            if f == 'x':
                pass
            else:
                word_flage_dict[w] = f
                print w,f
        data = json.dumps(word_flage_dict)
        file_to_store.write(data)
        file_to_store.write('\n')


file_to_store.close()
