import requests
from bs4 import BeautifulSoup
import re
import make_xlsx


# User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}


def GetAllUrl(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8' 
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # 篩選網址
    pattern = re.compile(r'^https://tw\.news\.yahoo\.com/%.*$')
    matching_urls = [a['href'] for a in soup.find("ul", {"class":"Z(0) Pos(r) W(100%) H(312px) Fz(16px) D(f)"}).find_all('a', href=pattern)]

    if matching_urls[0] == matching_urls[1]:
        return matching_urls[1:]
    #print(len(matching_urls))
    return matching_urls

def GetArticle(url):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8' 
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.find("h1").getText()


    article_lines = soup.find("div", {"class":"caas-body"}).find_all("p")
    article = ""
    for line in article_lines:
        line = line.getText()
        if line.find("看更多相關新聞") != -1:
            break
        article += line + "\n"
    #print(title)
    #print(article)
    return title, article



if __name__ == '__main__':
    # Yahoo奇摩新聞首頁
    url = "https://tw.news.yahoo.com/"  
    news_urls = GetAllUrl(url)
    FileName = "yahooNews.xlsx"
    make_xlsx.create_excel_file(FileName)
    articles = [["", "Topic Title", "Topic Link", "Topic Content"]]
    count = 0
    for news_url in news_urls:
        title, article = GetArticle(news_url)
        articles.append([count, title, news_url, article])
        count += 1
    make_xlsx.write_to_excel(FileName, articles)
    

