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


# ============== WEBSCRAPING FOR URLS ==============
links_list = []
book_list = []
# iterate through the first 25 pages of the new realeases catalogue
# change the url address for each page
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}

for page_number in range(0, 5):
    url = f'https://www.waterstones.com/campaign/new-books/sort/pub-date-desc/page/{page_number}'
    page = requests.get(url, headers=headers)
    # print(page.status_code)
    soup = BeautifulSoup(page.text, 'lxml')
    # print(soup.title.text)
    books = soup.find_all('div', {
        'class': 'title-wrap'})
    # print(len(books))
    # print(type(books))
    for items in books:
        book_url = 'https://www.waterstones.com' + \
            items.find('a', {'class': 'title link-invert dotdotdot'})['href']
        links_list.append(book_url)
print(links_list)
print(len(links_list))


# ============== WEBSCRAPING FOR BOOK INFO ==============
'''
for items in the links list --> 
vidsit each link -->
gather information and save to variables --> 
create book objects using variables as to populate fields. 
'''

# for index, link in enumerate(links_list):
url = link_list[1]
page = requests.get(url, headers=headers)
print(page.status_code)
soup = BeautifulSoup(page.text, 'lxml')
# print(soup.title.text)
book_id = index
print(book_id)
title = items.find(
    'a', {'class': 'title link-invert dotdotdot'}).text  # title div
print(title)
author = items.find(
    'a', {'class': 'title link-invert dotdotdot'}).text  # author div
print(author)
synopsis = items.find(
    'a', {'class': 'title link-invert dotdotdot'}).text  # synopsis div
print(synopsis)
link = link  # link from link list
print(link)
# image url from waterstones site
img = items.find('a', {'class': 'title link-invert dotdotdot'})['href']
print(img)
book_list.append(Book(book_id, title, author, synopsis, link, img))
