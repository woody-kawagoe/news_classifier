# 各カテゴリのニュース記事のURLを取得する
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS
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


def getNewslist(id, newslist):
    start_url = "https://gunosy.com/categories/"+str(id)
    page = ""
    news_number = 100
    if len(newslist) >= news_number:
        print("newslist length is over news_number", len(newslist))
        return newslist
    while len(newslist) < news_number:
        url = start_url+page
        try:
            html = urlopen(url)
        except HTTPError as e:
            print(e)
        else:
            bsObj = BS(html.read(), "html.parser")
            article_list = bsObj.find("div", {"class": "article_list"})\
                .findAll("div", {"class": "list_content"})
            for article in article_list:
                news_link = article.find("div", {"class": "list_title"})\
                    .find("a").attrs["href"]
                if news_link not in newslist:
                    newslist.append(news_link)
                if len(newslist) is news_number:
                    break
            page = bsObj.find("div", {"class": "pager-link-option"})\
                .find("a").attrs["href"]
            print(page, len(newslist), news_link)
    return newslist

for id, name in categories:
    print(id, name)
    path = 'trainer/newslist/'+name+'.csv'
    if os.path.exists(path):
        newslist = list(map(lambda x: x[:-1], open(path, 'r').readlines()))
        newslist = getNewslist(id, newslist)
    else:
        newslist = getNewslist(id, [])
    with open(path, 'w') as output:
        for url in newslist:
            output.write(url+'\n')
        print(name, "finish!")
        print("news length:", len(newslist))
