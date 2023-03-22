import requests
import lxml
from bs4 import BeautifulSoup
import tabulate


def view_all():
    book_data = []
    for books in book_list:
        book_data.append(shoes.__str__().split(','))
    return tabulate(book_data, tablefmt='outline') + '\n'


# ============== BOOK OBJECT ==============
class Book:
    def __init__(self, book_id, title, author, synopsis, link, img):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.synopsis = synopsis
        self.link = link
        self.img = img
    # __str__ returns each object as a string

    def __str__(self):
        return (f"{self.book_id},{self.title},{self.author},"
                + f"{self.synopsis},{self.link},{self.img}")


# ============== LISTS ==============
links_list = []
book_list = []
genre_list = []
all_genres = []


# ============== WEBSCRAPING FOR URLS ==============
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}

for page_number in range(0, 2):
    url = f'https://www.waterstones.com/campaign/new-books/sort/pub-date-desc/page/{page_number}'
    page = requests.get(url, headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'lxml')
    print(soup.title.text)
    books = soup.find_all('div', {
        'class': 'title-wrap'})
    print(len(books))
    print(type(books))
    for items in books:
        book_url = 'https://www.waterstones.com' + \
            items.find('a', {'class': 'title link-invert dotdotdot'})['href']
        links_list.append(book_url)
print(links_list)
print(len(links_list))

# ============== WEBSCRAPING FOR BOOK INFO ==============
for link in links_list:
    url = link
    page = requests.get(url, headers=headers)
    print(page.status_code)
    soup = BeautifulSoup(page.text, 'lxml')
    print(soup.title.text)
    title = soup.find(
        'span', {'class': 'book-title'}).text  # title div
    print(title)
    author = soup.find(
        'span', {'itemprop': 'author'}).text  # author div
    print(author)
    link = url  # link from link list
    print(link)
    # image url from waterstones site
    img = soup.find('img', {'itemprop': 'image'})['src']
    print(img)
    synopsis = soup.find(
        'div', {'id': 'scope_book_description'})  # synopsis div
    unwanted = synopsis.find('strong')
    if unwanted:
        unwanted.extract()
    else:
        None
    print(synopsis.text.strip())
    genre = soup.find(
        'div', {'class': 'breadcrumbs span12'})
    unwanted = (genre.find('strong'))
    unwanted.extract()
    unwanted = (genre.find('br'))
    unwanted.extract()
    genre = genre.text.strip()  # synopsis div
    remove_list = ['&', '\n', '>']
    for i in remove_list:
        genre = genre.replace(i, ',')
    genre = genre.split(',')
    genre = [items.strip() for items in genre]
    genre_list.append(genre)
    print(genre)

for i in genre_list:
    for j in i:
        if j in all_genres:
            pass
        else:
            all_genres.append(j)
print(all_genres)
# book_list.append(Book(title, author, synopsis, link, img))
