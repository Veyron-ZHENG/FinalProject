# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import json


with open('data_outcome/sentiment_score.json','r') as file:
    for line in file:
        if line == '\n':
            continue
        data = dict(json.loads(line.strip()))

positive_scores = []
negtive_scores = []
for aspect, scores in data.items():
    positive_scores.append(scores[0])
    negtive_scores.append(scores[1])


N = 7
positiveS = tuple(positive_scores)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, positiveS, width, color='r')

negtiveS = tuple(negtive_scores)
rects2 = ax.bar(ind+width, negtiveS, width, color='y')

ax.set_ylabel('Scores')
ax.set_title('The sentiment score to each aspect')
ax.set_xticks(ind+width)
ax.set_xticklabels( data.keys() )

ax.legend( (rects1[0], rects2[0]), ('Positive Score', 'Negtive Score') )

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()