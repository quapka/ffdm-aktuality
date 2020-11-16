import requests

from bs4 import BeautifulSoup

prog_url = "https://www.ffdm.cz/program/"
ffdm_page = requests.get(prog_url)

page_soup = BeautifulSoup(markup=ffdm_page.content, features='html.parser')

for header in page_soup.find_all('h2'):
    print(header.text)
    link = header.parent.parent.parent.parent.find('a')

    subpage = requests.get(link["href"])
    subpage_soup = BeautifulSoup(
        markup=subpage.content, features="html.parser")

    for item in subpage_soup.find_all("h2"):
        item_name = item.text
        item_link = 'link chybi'
        for _ in range(5):
            try:
                item_link = item.find('a')['href']
                break
            except TypeError:
                item = item.parent

        print("\t%s ---> %s" % (item_name, item_link))
