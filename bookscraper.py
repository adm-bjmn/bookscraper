import requests
import lxml
from bs4 import BeautifulSoup


links_list = []

# iterate through the first 25 pages of the new realeases catalogue
# change the url address for each page
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15'}

for page_number in range(0, 5):
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
