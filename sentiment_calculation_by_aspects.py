# -*- coding: utf-8 -*-
import json

def load_apect_feature(path):
    features = []
    with open(path,'r') as file:
        for line in file:
            if line == '\n':
                continue
            features.append(line.strip())
    features[0] = features[0][3:]
    return features

def load_sentiment_lexicon(path):
    opinion_words = []
    with open(path,'r') as file:
        for line in file:
            if line == '\n':
                continue
            opinion_words.append(line.strip())
    opinion_words[0] = opinion_words[0][3:]
    return opinion_words


color_features = load_apect_feature('Aspects/Color.txt')
material_features = load_apect_feature('Aspects/Material.txt')
price_features = load_apect_feature('Aspects/Price.txt')
quality_features = load_apect_feature('Aspects/Quality.txt')
service_features = load_apect_feature('Aspects/Service.txt')
size_features = load_apect_feature('Aspects/Size.txt')
style_features = load_apect_feature('Aspects/Style.txt')

color_opinions = []
material_opinions = []
price_opinions = []
quality_opinions = []
service_opinions = []
size_opinions = []
style_opinions = []


with open('data_outcome/bigrams.json','r') as file:
    for line in file:
        data = json.loads(line.strip())
        for word, opinion in data.items():
            if word.encode('utf-8') in color_features:
                color_opinions.append(opinion)
            if word.encode('utf-8') in material_features:
                material_opinions.append(opinion)
            if word.encode('utf-8') in price_features:
                price_opinions.append(opinion)
            if word.encode('utf-8') in quality_features:
                quality_opinions.append(opinion)
            if word.encode('utf-8') in service_features:
                service_opinions.append(opinion)
            if word.encode('utf-8') in size_features:
                size_opinions.append(opinion)
            if word.encode('utf-8') in style_features:
                style_opinions.append(opinion)

positive_opinions = load_sentiment_lexicon('sentiment/positive.txt')
negtive_opinions = load_sentiment_lexicon('sentiment/negtive.txt')
sentiment_scores = {}

sentiment_scores['color'] = [0,0]
for opinion in color_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['color'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['color'][1] += 1
print sentiment_scores['color']

sentiment_scores['material'] = [0,0]
for opinion in material_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['material'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['material'][1] += 1
print sentiment_scores['material']

sentiment_scores['price'] = [0,0]
for opinion in price_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['price'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['price'][1] += 1
print sentiment_scores['price']

sentiment_scores['quality'] = [0,0]
for opinion in quality_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['quality'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['quality'][1] += 1
print sentiment_scores['quality']

sentiment_scores['service'] = [0,0]
for opinion in service_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['service'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['service'][1] += 1
print sentiment_scores['service']

sentiment_scores['size'] = [0,0]
for opinion in size_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['size'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['size'][1] += 1
print sentiment_scores['size']

sentiment_scores['style'] = [0,0]
for opinion in style_opinions:
    if opinion.encode('utf-8') in positive_opinions:
        sentiment_scores['style'][0] += 1
    if opinion.encode('utf-8') in negtive_opinions:
        sentiment_scores['style'][1] += 1
print sentiment_scores['style']

data = json.dumps(sentiment_scores)
with open('data_outcome/sentiment_score.json','w') as file:
    file.write(data)