import requests

from bs4 import BeautifulSoup


def get_tags(url, tag):
    page = requests.get(url)
    soup = BeautifulSoup(markup=page.content, features='html.parser')
    return soup.find_all(tag)


def print_page_info(url, format, cont=None, max_iter=5, tag='h2'):
    for header in get_tags(url, tag):
        name = header.text
        link = 'Link chybi'
        for _ in range(max_iter):
            try:
                link = header.find('a')['href']
                break
            except TypeError:
                header = header.parent
        print(format.replace('{name}', name).replace('{link}', link))
        if (cont):
            print_page_info(link, cont, max_iter=max_iter, tag=tag)


prog_url = "https://www.ffdm.cz/program/"
print_page_info(prog_url, '{name}:', cont='\t{name} ---> {link}')
