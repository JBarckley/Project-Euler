import requests
from pprint import pprint
from bs4 import BeautifulSoup


def main():
    titles = []
    prices = []
    links = []
    books = []

    for i in range(1, 51):
        r = requests.get('http://books.toscrape.com/catalogue/page-' + str(i) + '.html')
        soup = BeautifulSoup(r.text, 'html.parser')
        img = soup.ol.find_all("a")
        pce = soup.ol.find_all("p")
        for title in img:
            if title.get('title') is not None:
                titles.append(title.get('title'))
                links.append(title.get('href'))
        for price in pce:
            if price['class'] == ['price_color']:
                prices.append(price.string)
        print("page: " + str(i))

    for k in range(0, len(titles)):
        books.append([titles[k], prices[k], links[k]])

    print(books)


main()
