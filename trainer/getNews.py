# ニュースのURLリストを元に、各カテゴリのニュースのBoWを取得する
from subprocess import Popen, PIPE
import os.path

categories = [
    ["1", "エンタメ"],
    ["2", "スポーツ"],
    ["3", "おもしろ"],
    ["4", "国内"],
    ["5", "海外"],
    ["6", "コラム"],
    ["7", "IT・科学"],
    ["8", "グルメ"]
]


def getNews(newslist):
    news = ""
    for news_url in newslist:
        p = Popen(["python", "trainer/getBoW.py", news_url], stdout=PIPE)
        c = p.stdout.readlines()
        if c:
            bow = c[0].decode('utf-8')
        else:
            bow = ""
        print(news_url, bow[:10], "...")
        news = news+bow+"\n"
    return news

for id, name in categories:
    print(id, name)
    path = 'trainer/newslist/'+name+'.csv'
    if os.path.exists(path):
        newslist = list(map(lambda x: x[:-1], open(path, 'r').readlines()))
    else:
        print("not found!", path)
    path = 'trainer/news/'+name+'.csv'
    if os.path.exists(path):
        if len(open(path, 'r').readlines()) is 100:
            print("already get", name, "100 news")
    else:
        news = getNews(newslist)
        open(path, 'w').write(news)
