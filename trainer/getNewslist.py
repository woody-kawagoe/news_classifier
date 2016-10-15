# 各カテゴリのニュース記事のURLを取得する
import os.path
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup as BS


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


def getNewslistByCategory(id, newslist):
    start_url = "https://gunosy.com/categories/"+str(id)
    page = ""
    news_number = 100
    if len(newslist) >= news_number:
        print("newslist length is over news_number", len(newslist))
        return newslist
    while len(newslist) < news_number:
        url = start_url+page
        try:
            html = requests.get(url)
        except RequestExceptiona as e:
            print(e)
        else:
            bsObj = BS(html.text, "html.parser")
            article_list = bsObj.find("div", {"class": "article_list"})\
                .findAll("div", {"class": "list_content"})
            for article in article_list:
                news_link = article.find("div", {"class": "list_title"})\
                    .find("a").attrs["href"]
                if news_link not in newslist:
                    newslist.append(news_link)
                if len(newslist) == news_number:
                    break
            page = bsObj.find("div", {"class": "pager-link-option"})\
                .find("a").attrs["href"]
            print(page, len(newslist), news_link)
    return newslist


def getNewslist():
    for id, name in categories:
        print(id, name)
        path = 'trainer/newslist/'+name+'.csv'
        if os.path.exists(path):
            newslist = list(map(lambda x: x[:-1], open(path, 'r').readlines()))
            newslist = getNewslistByCategory(id, newslist)
        else:
            newslist = getNewslistByCategory(id, [])
        with open(path, 'w') as output:
            for url in newslist:
                output.write(url+'\n')
            print(name, "finish!")
            print("news length:", len(newslist))

if __name__ == "__main__":
    getNewslist()
