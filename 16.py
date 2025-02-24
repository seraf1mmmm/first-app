import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

book_titles = []

for page_num in range(1, 51):
    url = base_url.format(page_num)
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('h3')
        for book in books:
            title = book.find('a')['title']
            book_titles.append(title)
    else:
        print(f"Не вдалося отримати дані з сторінки {page_num}")

for idx, title in enumerate(book_titles, 1):
    print(f"{idx}. {title}")
