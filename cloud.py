# -*- coding:utf-8 -*-
import os
import matplotlib.pyplot as plt
import sys
sys.path.append('.pyenv/versions/anaconda3-4.3.1/envs/py3.6.0/lib/python3.6/site-packages')
from wordcloud import WordCloud
import numpy as np

with open("corpus.txt","rb")as f:
    binarydata = f.read()
    text = binarydata.decode('utf-8')
wordcloud = WordCloud(background_color="white",
                  font_path="NotoSansCJKsc-Bold",
                  width=1920,
                  height=1080)
# テキストからワードクラウドを生成する。
wordcloud.generate(text)
# ファイルに保存する。
wordcloud.to_file('wordcloud-1.png')
# numpy 配列で取得する。
img = wordcloud.to_array()
print(img.shape)
