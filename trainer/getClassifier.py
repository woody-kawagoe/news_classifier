# ニュースのBoWから分類器を作成する
from subprocess import Popen, PIPE
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS
import os.path
import pandas as pd
import math

categories=[
    "entertainment",
    "sports",
    "omosiro",
    "domestic",
    "oveasea",
    "column",
    "technology",
    "gourmet"
]

def getWordcount(name):
    path='trainer/news/'+name+'.csv'
    wordcount={}
    if os.path.exists(path):
        wordlist=open(path,'r').read().replace("\n"," ").split(" ")
        for word in wordlist:
            if word in wordcount:
                wordcount[word]+=1
            else:
                wordcount[word]=1
    else:
        print("not found!",path)
    return wordcount

wordcount={}
words=[]
for name in categories:
    wordcount[name]=getWordcount(name)
    words.extend(getWordcount(name))
print(len(words))
words=list(set(words))
print(len(words))

classifier=pd.DataFrame(index=words,columns=categories)
for word in words:
    for name in categories:
        if word in wordcount[name]:
            count=wordcount[name][word]
        else:
            count=0
        cat_len=float(len(wordcount[name]))
        #classifier.ix[word,name]=count
        classifier.ix[word,name]=math.log((count+1)/cat_len) 
classifier.to_csv("trainer/classifier.csv")
print("finish output csv")
