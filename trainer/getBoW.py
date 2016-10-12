import sys
import MeCab
from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup as BS


def getArticle(url):
    try:
        html=urlopen(url)
    except HTTPError as e:
        #print(e)
        return 0
    except URLError as e:
        #print(e)
        return 0
    else:
        bsObj=BS(html.read(),"html.parser")
        article=bsObj.find("div",{"class","article"}).get_text()
        #print(article)
        return article

def validate(node,line):
    stop_words = [
            r'接尾',
            r'接頭',
            r'非自立',
            r'代名詞',
            r'数',
            r'記号',
            r'ない',
            r'する'
            ]
    for stop_word in stop_words:
        if stop_word in node:
            return False
    features = [
            r'形容詞',
            r'動詞',
            r'名詞'
            ]
    for feature in features:
        if feature in line:
            return True
    return False

def getBoW(text,tagger):
    nodes=tagger.parse(text)
    nouns=[]
    for node in nodes.splitlines()[:-1]:
        line = node.replace('-','\t').split('\t')
        if validate(node,line):
            nouns.append(line[2])
    return nouns

argvs=sys.argv
url=argvs[1]
article=getArticle(url)
if not article is 0:
    tagger=MeCab.Tagger("-Ochasen -d /usr/lib64/mecab/dic/mecab-ipadic-neologd")
    BoW=getBoW(article,tagger)
    for w in BoW:
        print(w,end=" ")
