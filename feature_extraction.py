# -*- coding: utf-8 -*-

import jieba.posseg as pseg
import jieba
import jieba.analyse
import json

t = 0

word_freq_dict = {}
num = 0
with open('data_outcome/data_preprocessed.json','r') as file:
    for line in file:
        if line == '\n':
            continue
        data = json.loads(line.strip())
        for word in data:
            if data[word] == 'feature':
                if word_freq_dict.has_key(word):
                    word_freq_dict[word] += 1
                else:
                    word_freq_dict[word] = 1

file_to_store = open("data_outcome/features_dict.json",'w')
for word, freq in word_freq_dict.items():
    if freq > t:
        file_to_store.write(word.encode('utf-8')+' feature')
        file_to_store.write("\n")