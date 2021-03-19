import requests
from bs4 import BeautifulSoup
import string


def parse_url(url):
    return BeautifulSoup(requests.get(url).content, 'html.parser')


def open_link(link):
    url_art = 'https://www.nature.com' + link
    soup = parse_url(url_art)
    body = soup.find('div', {'class': 'article__body'}).text.strip()
    title = soup.find('title').text
    d = list(title)
    for i in range(len(d)-1):
        if d[i] in string.punctuation:
            d[i] = ' '
    for i in range(len(d) - 1):
        if d[i] == ' ':
            d[i] = '_'
    title = "".join(d)
    save_to_txt(body, title)


def save_to_txt(content, name):
    with open(name + '.txt', 'w', encoding='utf-8') as file:
        file.write(content)
        file.close()
    print('Article "' + name + '.txt" saved')


def search_for_news(src):
    all_art = src.find_all('article')
    for art in all_art:
        temp = art.find('span', {'class': 'c-meta__type'}).text
        if 'News' in temp:
        # if temp == 'News':
            link = art.find('a')
            open_link(link.get('href'))


def main():
    url = str('https://www.nature.com/nature/articles')
    soup = parse_url(url)
    search_for_news(soup)


if __name__ == '__main__':
    main()
