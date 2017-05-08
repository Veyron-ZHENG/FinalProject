# -*- coding: utf-8 -*-

import jieba.posseg as pseg
import jieba.analyse
import json

jieba.load_userdict("data_outcome/features_dict.txt")
jieba.analyse.set_stop_words('stopwords.txt')

def position_gen(maxi):
    sign = -1
    for i in range(1,maxi+1):
        for j in range(2):
            yield sign*i
            sign = (-1)*sign


def find_nearest_adjective(line,word):
    word_flag_list = []
    word_flag = pseg.cut(line)
    for w, f in word_flag:
        word_flag_dict = [w,f]
        word_flag_list.append(word_flag_dict)

    index = 0
    for i in range(len(word_flag_list)):
        if word_flag_list[i][0].encode('utf-8') == word.encode('utf-8'):
            index = i
            break

    if index == 0:
        for i in range(1,len(word_flag_list)):
            if word_flag_list[i][1] == 'a':
                return word_flag_list[i][0]

    elif index == (len(word_flag_list)-1):
        indexs = range(len(word_flag_list)-1)
        indexs.reverse()
        for i in indexs:
            if word_flag_list[i][1] == 'a':
                return word_flag_list[i][0]

    else:
        max_bias = min(index,len(word_flag_list)-index-1)
        positions_bias = position_gen(max_bias)
        flag_for_index = 0
        for i in positions_bias:
            if word_flag_list[index+i][1] == 'a':
                return word_flag_list[index+i][0]
            if (index+i) == 0:
                flag_for_index = 0
            elif (index+i) == (len(word_flag_list)-1):
                flag_for_index = 1

        if flag_for_index == 0:
            for i in range(index+1,len(word_flag_list)):
                if word_flag_list[i][1] == 'a':
                    return word_flag_list[i][0]
        elif flag_for_index == 1:
            indexs = range(index)
            indexs.reverse()
            for i in indexs:
                if word_flag_list[i][1] == 'a':
                    return word_flag_list[i][0]


features = []
with open('data_outcome/features_dict.txt','r') as file:
    for line in file:
        if line == '\n':
            continue
        features.append(line.strip().split(' ')[0])

features[0] = '款式'

file_to_store = open('data_outcome/bigrams.json','w')
file_opinion_words = open('sentiment/opinion_words.txt','w')
opinion_words = []
with open('reviews.txt','r') as file:
    for line in file:
        words = list(jieba.cut(line))
        for word in words:
            if word.encode('utf-8') in features:
                adj = find_nearest_adjective(line,word)
                if adj == None:
                    continue
                data = json.dumps({word:adj})
                # file_to_store.write(word.encode('utf-8')+' '+adj.encode('utf-8'))
                file_to_store.write(data)
                file_to_store.write('\n')
                if adj not in opinion_words:
                    opinion_words.append(adj)
    # cutlist_chi = ['，','。','、','！','？','~','’']
    # cutlist_eng = [',','.','?','!',' ']
    # cutlist = u'，。、！？~’'
    # for line in file:
    #     for word in re.split(cutlist,deunicode(line)):
    #         print word

for word in opinion_words:
    file_opinion_words.write(word.encode('utf-8'))
    file_opinion_words.write('\n')
file_opinion_words.close()
file_to_store.close()
