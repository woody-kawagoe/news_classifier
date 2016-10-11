from subprocess import Popen, PIPE
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as BS

categories=[
    ["1","entertainment"],
    ["2","sports"],
    ["3","omosiro"],
    ["4","domestic"],
    ["5","oveasea"],
    ["6","column"],
    ["7","technology"],
    ["8","gourmet"]
]

def getNewslist(id):
    start_url="https://gunosy.com/categories/"+str(id)
    page=""
    newslist=[]
    news_number=100
    while len(newslist) < news_number:
        url=start_url+page
        try:
            html=urlopen(url)
        except HTTPError as e:
            print(e)
        else:
            bsObj=BS(html.read(),"html.parser")
            article_list=bsObj.find("div",{"class":"article_list"}).findAll("div",{"class":"list_content"})
            for article in article_list:
                news_link=article.find("div",{"class":"list_title"}).find("a").attrs["href"]
                newslist.append(news_link)
            page=bsObj.find("div",{"class":"pager-link-option"}).find("a").attrs["href"]
    return newslist

def getNews(newslist):
    news=""
    for news_url in newslist:
        p=Popen(["python","trainer/getBoW.py",news_url],stdout=PIPE)
        c=p.stdout.readlines()
        bow=c[0].decode('utf-8')
        print(bow)
        news=news+bow+"\n"
    return news

for d,name in categories:
    print(id,name)
    newslist=getNewslist(id)
    open('trainer/list-'+name+'.csv','w').write(newslist)
    news=getNews(newslist)
    open('trainer/'+name+'.csv','w').write(news)
