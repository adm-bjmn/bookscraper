import requests
import lxml
from bs4 import BeautifulSoup
from tabulate import tabulate


def view_all():
    book_data = []
    for books in book_list:
        book_data.append(books.__str__().split(','))
    return print(tabulate(book_data, tablefmt='outline') + '\n')


# ============== BOOK OBJECT ==============
class Book:
    def __init__(self, title, author, publish_date, synopsis, link, img, genre):
        self.title = title
        self.author = author
        self.publish_date = publish_date
        self.synopsis = synopsis
        self.link = link
        self.img = img
        self.genre = genre
    # __str__ returns each object as a string

    def __str__(self):
        return (f",{self.title},{self.author},{self.publish_date}"
                + f"{self.synopsis},{self.link},{self.img},{self.genre}")


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
# for link in links_list:
# url = link
url = links_list[1]
page = requests.get(url, headers=headers)
print(page.status_code)
soup = BeautifulSoup(page.text, 'lxml')
book_info = []
print(soup.title.text)

# == Title ==
title = soup.find(
    'span', {'class': 'book-title'}).text
book_info.append(title)
print(title)

# == Author ==
author = soup.find(
    'span', {'itemprop': 'author'}).text
book_info.append(author)
print(author)

# == Publish Date ==
publish_date = soup.find(
    'meta', {'itemprop': 'datePublished'})['content']
book_info.append(publish_date)
print(publish_date)

# == Synopsis ==
synopsis = soup.find(
    'div', {'id': 'scope_book_description'})
unwanted = synopsis.find('strong')
if unwanted:
    unwanted.extract()
else:
    None
print(synopsis.text.strip())
book_info.append(synopsis.text.strip().replace('\n', ' '))

# == Link ==
link = url
print(link)
book_info.append(link)

# == Image ==
img = soup.find('img', {'itemprop': 'image'})['src']
book_info.append(img)
print(img)

# == Genre ==
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
genre = [items.strip().replace(' ', '').lower() for items in genre]
genre_list.append(genre)
# if 'travel' in genre:
# print('oui madam')
book_info.append(' '.join(genre))
print('========  OBJECT  ========= ')


book = Book(book_info[0], book_info[1], book_info[2],
            book_info[3], book_info[4], book_info[5], book_info[6])

print(book.__str__())

'''
for i in genre_list:
    for j in i:
        if j in all_genres:
            pass
        else:
            all_genres.append(j)
print(all_genres)
'''
