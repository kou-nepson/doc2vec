import os
import shutil
import MeCab
import sys
import re

m = MeCab.Tagger("-Owakati")
sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")

path = os.getcwd()
path += "/data"#あらかじめ"data"という名前のディレクトリが必要
files = os.listdir(path)
print(files)
files.pop(0) #.DS_Storeを削除
corpus = ""

for i in files:
    print(str(i))
    if str(i[-4:]) == ".txt":
        with open("data/"+str(i)+"","rb") as f:
            binarydata = f.read()
            text = binarydata.decode('shift_jis')
            # ルビ、注釈などの除去
            text = re.split(r'\-{5,}', text)[2]
            text = re.split(r'底本：', text)[0]
            text = re.sub(r'《.+?》', '', text)
            text = re.sub(r'［＃.+?］', '', text)
            text = re.sub(r'「','',text)
            text = re.sub(r'」','',text)
            text = re.sub(r'、','',text)
            text = re.sub(r'。','',text)
            text = re.sub(r'？','',text)
            text = re.sub(r'！','',text)
            text = re.sub(r'…','',text)
            text = re.sub(r'（','',text)
            text = re.sub(r'）','',text)
            text = re.sub(r'\n','',text)
            text = re.sub(r'\r','',text)
            newpath = path + "/" + re.sub(r'.txt','',str(i))
            if os.path.exists(newpath) == False:
                os.mkdir(newpath)
            if os.path.exists(newpath+".txt") == True:
                print("dataディレクトリを整理します")
                shutil.move(newpath+".txt", newpath)
        result = ""
        with open(""+str(newpath) + "/wakachi.txt", "w") as g:
           text1 = text.splitlines()
           for t in text1:
               result += m.parse(t)
           print("nowrodding... "+str(i)+"")
           g.write(str(result)) # skip first \s
           corpus += result

if corpus != "":
    with open("corpus.txt","a") as f:
        f.write(corpus)
else :
    print("新しいデータはありません")#新しく読み込んだファイルがなければそのまま終了

