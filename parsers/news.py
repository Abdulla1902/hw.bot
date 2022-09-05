import requests
from bs4 import BeautifulSoup


URL = 'https://kaktus.media/?lable=8&date=2022-09-05&order=time'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ArticleItem--data ArticleItem--data--withImage')
    news = []
    for item in items:
        news.append({
            'title': item.find('a', class_="ArticleItem--name").getText().replace('\n', ''),
            'time': item.find('div', class_='ArticleItem--time').getText().replace('\n', ''),
            'link': item.find('a', class_="ArticleItem--name").get('href')
        })
    return news


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(0, 1):
            html = get_html(f'{URL}page/{page}/')
            answer.extend(get_data(html.text))
        return answer
    raise Exception("Error in parsers")
# def get_data(html):
#     soup = BeautifulSoup(html, 'html.parsers')
#     items = soup.find_all('a', class_='article-card inline-card')
#     anime = []
#     for item in items:
#         data = item.find('div', class_='article-card-details').find('time').getText().split(', ')
#         anime.append({
#          'title': item.find('div', class_='article-card-details').find('h2').getText(),
#          'time': data[0],
#          'year': data[1],
#          'link': item.find('div', class_='article-card-details').find('h2').get('href')
#         })
#     print(anime)


html = get_html(URL)
get_data(html.text)






