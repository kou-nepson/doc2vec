import requests
import bs4
import re
import MeCab
import sys

m = MeCab.Tagger("-Owakati")
sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")

userurl = 'https://twitter.com/TWITTERID'#ツイートを取得したいユーザーのID
html = requests.get(userurl)
if html.status_code == 404:
    print('ユーザーがいません')
    exit()
soup = bs4.BeautifulSoup(html.text, 'html.parser')
tweets = soup.select('.js-stream-item')
result = ""
for n,l in enumerate(tweets):
    print(l.p.text)
    result += str(l.p.text)

result = re.sub(r'\r','',result)
result = re.sub(r'\n','',result)

corpus = m.parse(result)

with open("nhightweet.txt", "w") as f:
    f.write(corpus)

with open("corpus.txt") as g:
    l = g.readlines()

l.insert(0, corpus)

with open("corpus.txt","w") as f:
    f.writelines(l)
