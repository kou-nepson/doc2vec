import requests
import bs4
import re

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

with open("tweet.txt", "w") as f:
    f.write(result)



