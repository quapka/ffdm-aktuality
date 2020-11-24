import requests

from bs4 import BeautifulSoup


def get_tags(url, tag):
    # Stáhne stránku (url) z internetu
    # vrátí všechny výskyty daného html tagu (tag) (jako ResultSet)
    page = requests.get(url)
    soup = BeautifulSoup(markup=page.content, features='html.parser')
    return soup.find_all(tag)


def print_page_info(url, format, cont=None, max_iter=5, tag='h2'):
    # Vytiskne text v daném formátu z informací získaných na stránce (url)
    # Pokud cont obsahuje další text s formátem, bude tato funkce zavolána
    # rekurzivně znovu s url nalezenou na stránce nejblíže k tagu s tímto
    # formátem (cont)
    # Formát: '{name}' : bude nahrazeno textem v tagu
    #         '{link}' : bude nahrazeno linkem nejblíže k tagu
    for header in get_tags(url, tag):
        # Získávání informací k tagu
        name = header.text
        link = 'Link chybi'
        for _ in range(max_iter):
            # Získávání linku nejblíže k tagu (s omezením max_iter)
            try:
                link = header.find('a')['href']
                break
            except TypeError:
                header = header.parent
        # Tisk, nahrazování klíčových slov
        print(format.replace('{name}', name).replace('{link}', link), end='')
        if (cont):
            # Rekurzivní volání funkce pokud cont něco obsahuje
            print_page_info(link, cont, max_iter=max_iter, tag=tag)


# stránka ffdm
prog_url = "https://www.ffdm.cz/program/"
# tisk informací ze stránky
print_page_info(prog_url, '{name}:\n', cont='\t{name} ---> {link}\n')
# čekání na enter :)
input()
