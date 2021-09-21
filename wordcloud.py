'''
author: Xueshan Zhang
date  : 2021/9/21 Happy Mid Autumn Festival to all and also myself :)
'''

import os
import re
import collections
import imageio
import numpy as np
import jieba
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread

# 1. read file
f = open('C://Users//Administrator//Desktop//practice.txt','rt')
fd = f.read()
# >> f = open('C://Users//Administrator//Desktop//practice.txt', 'rt').read()
f.close()
# >> f = open('C://Users//Administrator//Desktop//practice_2.txt',encoding='gbk').read()
# >> f = open('C://Users//Administrator//Desktop//practice_2.csv',encoding='utf-8').read()
# >> fd = open('C://Users//Administrator//Desktop//practice.txt', 'rt').read()

# 2. preprocess file content
pattern = re.compile(u'\t|\'|\n|\.|-|_|#|：|:|；|\||/||(|)|\?|"')
fd = re.sub(pattern, '', fd)

seg = jieba.cut(fd, cut_all=False)
# print(type(seg))
# print(seg)

# rwlist = [line.strip() for line in open('C://Users//Administrator//Desktop//rw.txt').readlines()]
# rwlist = [rw.strip() for rw in open('C://Users//Administrator//Desktop//rw.txt').read()]
rwlist = [u'-', ' ', 'u', '@', ',', u'( ', u')']

# 3. process file content
words = []
for word in seg:
    if word not in rwlist and len(word) >= 1:
        words.append(word.replace(' ', ''))
        # words.append(word)
cloud_text = ",".join(words)
# cloud_text = words

# 4. collect word counts
count = collections.Counter(cloud_text)
count_top5 = count.most_common(5)
print(type(count_top5))
for i in count_top5:
    print('character: ', i[0], ';', 'count: ', i[1])

# 5. generate wordcloud
# 5.1 without background & generate
wc = WordCloud(
    background_color='white',
    width=900,
    height=600,
    max_words=100,
    max_font_size=99,
    min_font_size=16,
    random_state=50
).generate(fd)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig("C://Users//Administrator//Desktop//wordcloud.jpg")
plt.show()
#
# 5.2 without background & generate from frequency
wc = WordCloud(
    background_color='white',
    width=900,
    height=600,
    max_words=100,
    max_font_size=99,
    min_font_size=16,
    random_state=50
).generate_from_frequencies(count)
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig("C://Users//Administrator//Desktop//wordcloud1.jpg")
plt.show()
#
# 5.3 with background
jpg = imread('C://Users//Administrator//Desktop//image.jpg')

wc = WordCloud(
    mask = jpg,
    background_color="white",
    width = 1500,
    height = 960,
    margin = 10
).generate(cloud_text)
plt.imshow(wc)
plt.axis("off")
plt.savefig("C://Users//Administrator//Desktop//wordcloud2.jpg")
plt.show()
