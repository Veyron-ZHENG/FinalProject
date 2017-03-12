# -*- coding: utf-8 -*-

import json
import re

void_review=['评价方未及时做出评价,系统默认好评!','此用户没有填写评价。','15天内买家未作出评价']

with open('reviews.txt','w') as file_to_store:
    reviews = []
    for page_num in range(1, 251):
        with open('Taobao\\item' + str(page_num) + '.json', 'r') as item_file:
            content = re.findall(r'<p>\w+\((.*)\)</p>', item_file.read())[0]
            data = json.loads(content)
            comments = data["comments"]
            for comment in comments:
                if comment["content"].encode("utf-8") not in void_review:
                    reviews.append((comment["content"]+'\n').encode('utf-8'))
                try:
                    for append_comment in comment["appendList"]:
                        if append_comment["content"].encode("utf-8") not in void_review:
                            reviews.append((append_comment["content"]+'\n').encode('utf-8'))
                except:
                    pass
    file_to_store.writelines(reviews)