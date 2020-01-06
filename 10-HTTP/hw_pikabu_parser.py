import requests
from collections import Counter
from bs4 import BeautifulSoup as bs


url = 'https://pikabu.ru/new?page='

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                     'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/79.0.3945.88 Safari/537.36'}

_cookies = {"name": "pkbRem",
            "value": "%7B%22uid%22%3A3045523%2C%22username%22%3A%22ausoseastre%22%2C%22rem%22%3A%22e688505b68f2541098edb8b2ab1d2864%22%2C%22tries%22%3A0%7D"}

tags_list = list()


def picabu_parser(url, headers):

    session = requests.Session()
    session.cookies.set(**_cookies)
    request = session.get(url, headers=headers)

    page = 0
    if request.status_code == 200:
        while page != 10:
            request = session.get(url + str(page), headers=headers)
            soup = bs(request.content, 'html.parser')
            divs = soup.find_all('div', attrs={'class': "story__tags tags"})
            for div in divs:
                tag = div.find('a', attrs={'class': "tags__tag"}).text
                tags_list.append(tag)
            page += 1
    else:
        print('Error')


if __name__ == "__main__":
    picabu_parser(url, headers)
    Counter(tags_list).most_common(10)

    with open('pikabuTop.txt', 'w', encoding='utf8') as file:
        file.write('------------\nTop 10 tags\n------------\n')
        for tag in Counter(tags_list).most_common(10):
            file.write(f'{tag[0]}: {tag[1]}\n')
