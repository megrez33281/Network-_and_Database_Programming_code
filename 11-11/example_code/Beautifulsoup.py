#  參考 https://www.youtube.com/watch?v=9Z9xKWfNo7k&t=72s  基本教學
# install beautifulsoup4 using "pip install beautifulsoup4" 以解析網頁
import urllib.request as req
import bs4
url="https://www.ptt.cc/bbs/movie/index.html"
#一header讓Crawler看起來像是一般人的Request
Request=req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    })
with req.urlopen(Request) as response:
    data=response.read().decode("utf-8")

#使用html來解析data 字串
root=bs4.BeautifulSoup(data, "html.parser")
#尋找class=title 的div
titles=root.find_all("div", class_="title")    

#for title in titles: 
#    print(title.a.string) #只抓<a>標籤下的string clear

titles=root.find_all("div", class_="title")
for title in titles: 
    if "本文已被刪除" in str(title):
        print('文章被刪除了，列印不出來') 
    else:
        print(title.a.string) #只抓<a>標籤下的string