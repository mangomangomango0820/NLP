import os
import re
import collections
import imageio
import numpy as np
import jieba
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from imageio import imread

# 1. read file
f = open('C://Users//Administrator//Desktop//practice.txt','rt')
fd = f.read()
# f = open('C://Users//Administrator//Desktop//practice.txt', 'rt').read()
f.close()

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

# 5. image process & generaate wordcloud
jpg = imread('C://Users//Administrator//Desktop//image.png')

wc = WordCloud(
    mask = jpg,
    background_color="white",
    width = 1500,
    height = 960,
    margin = 10
).generate(cloud_text)

plt.imshow(wc)
plt.axis("off")
plt.savefig("C://Users//Administrator//Desktop//wordcloud.jpg")
plt.show()