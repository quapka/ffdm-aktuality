import requests

from bs4 import BeautifulSoup


def color_print(string: str, end='\n'):
    # Funkce vypíče text v daném stylu za pomocí ANSI Escape kódů
    # Na windows je potřeba použít windows terminal aby funkce fungovala správně
    # (defaultní cmd a Power-Shell nepodporují ANSI Escape kódy)
    # Neměl jsem možnost testovat na Unix
    #
    # Pro nostavení barvy se ve stringu použije §sfb
    # s nastaví styl textu (hodnota 0 - 9, c)
    # f nastaví popředí text (hodnota 0 - 7)
    # b nastaví pozadí textu (hodnota 0 - 7, x)
    # Vždy musí být definovány všechny 3 parametry
    #
    # x na pozici pozadí: zruší/resetuje pozadí textu
    #
    # styl textu:
    # 0 normální text
    # 1 Windows: světlejší text | Unix: tučný text
    # 2 Windows: tmavší text    | Unix: tenký text
    # 3 Windows: normální text  | Unix: ?
    # 4 podtržený text
    # 5 Windows: blikající text | Unix: ?
    # 6 Windows: blikající text | Unix: ?
    # 7 Invertovaný text
    # 8 Neviditelný text (barva textu = barva pozadí)
    # 9 Windows: normální text  | Unix: přeškrtlý text
    # c Resetuje barvy, nezáleží na hodnotě na pozici 'f' a 'b'
    #
    # Barvy:
    # 0 Černá
    # 1 Červená
    # 2 Zelená
    # 3 žlutá
    # 4 Modrá
    # 5 Fialová
    # 6 Tyrkysová
    # 7 Bílá

    # Rozdělení textu na sekce podle barev
    col = string.split(sep='§')
    # Vypsání textu na začátku co nemá barvu
    print(col.pop(0), end='')
    for text in col:
        # Pokud na začátku sekce nejsou tři definované hodnoty, nevypisuj
        if (len(text) < 3):
            continue
        # Oddělení stylu, popředí, pozadí a samotného textu
        styl = text[0]
        fore = text[1]
        back = text[2]
        text = text[3:len(text)]
        # Ošetření špatného vstupu a speciálních možností
        if (styl.lower() == 'c'):
            # Výpis při resetu
            print(text, end='')
            continue
        try:
            if (int(styl) > 8):
                styl = '0'
        except Exception:
            styl = '0'
        try:
            if (int(fore) > 7):
                fore = '7'
        except Exception:
            fore = '7'
        if (back.lower() == 'x'):
            # Výpis při zrušeném pozadí
            print(('\x1b[%s;3%sm%s\x1b[0m' % (styl, fore, text)), end='')
            continue
        try:
            if (int(back) > 7):
                back = '0'
        except Exception:
            back = '0'
        # Výpis textu s barvami
        print(('\x1b[%s;3%s;4%sm%s\x1b[0m' % (styl, fore, back, text)), end='')
    print(end, end='')


def get_tags(url, tag):
    # Stáhne stránku (url) z internetu
    # vrátí všechny výskyty daného html tagu (tag) (jako ResultSet)
    page = requests.get(url)
    soup = BeautifulSoup(markup=page.content, features='html.parser')
    return soup.find_all(tag)


def print_page_info(url, format, cont=None, max_iter=5, tag='h2', nolink_msg='Link Chybi', colors=False):
    # Vytiskne text v daném formátu z informací získaných na stránce (url)
    # Pokud cont obsahuje další text s formátem, bude tato funkce zavolána
    # rekurzivně znovu s url nalezenou na stránce nejblíže k tagu s tímto
    # formátem (cont)
    # Formát: '{name}' : bude nahrazeno textem v tagu
    #         '{link}' : bude nahrazeno linkem nejblíže k tagu
    for header in get_tags(url, tag):
        # Získávání informací k tagu
        name = header.text
        link = nolink_msg
        for _ in range(max_iter):
            # Získávání linku nejblíže k tagu (s omezením max_iter)
            try:
                link = header.find('a')['href']
                break
            except TypeError:
                header = header.parent
        # Tisk, nahrazování klíčových slov
        if (colors):
            color_print(format.replace('{name}', name).replace('{link}', link), end='')
        else:
            print(format.replace('{name}', name).replace('{link}', link), end='')
        if (cont):
            # Rekurzivní volání funkce pokud cont něco obsahuje
            print_page_info(link, cont, max_iter=max_iter, tag=tag, nolink_msg=nolink_msg, colors=colors)


# stránka ffdm
prog_url = "https://www.ffdm.cz/program/"
# tisk informací ze stránky s barvami
print_page_info(prog_url, '§32x{name}:\n', cont='\t§03x{name} §07x---> §04x{link}\n', nolink_msg='§01xLink Chybi', colors=True)
