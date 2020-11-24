# O repozitáři
V tomto repozitáři je ukázková aplikace pro [Programovací workshop #1](https://www.ffdm.cz/programovaci-workshop/) v rámci XVI. FFDM.

# O aplikaci

Cílem této aplikace je posbírat (angl. scrape) informace z webu [FFDM](https://www.ffdm.cz) o aktuálním programu a zobrazit je uživateli.

# Spuštění
Pro spuštění potřebujete mít nainstalovaný Python 3. Dále musíte vytvořit a aktivovat tzv. virtuální prostředí (angl. virtual environment). Konkrétní kroky na Unix platformě:
```
$ python3 -m venv virtual
$ source virtual/bin/activate
(virtual) $ python ffdm-aktuality.py
Streamy
	Warm Up Stream ---> https://www.facebook.com/events/2804834203127659
	XVI. FFDM Stream ---> link chybi
	Bohoslužba ---> link chybi
Filmy
	NEW: Naše planeta E01 ---> https://www.ffdm.cz/nase-planeta-e01/
	NEW: Amadeus ---> https://www.ffdm.cz/film-zive/
	NEW: The Peanut Butter Falcon ---> https://www.ffdm.cz/the-peanut-butter-falcon/
	Sametová revoluce – dokument + online debata s Šimonem Pánkem ---> https://www.ffdm.cz/sametova-revoluce-dokument-online-debata-s-simonem-pankem/
	Rozpuštěný a vypuštěný ---> https://www.ffdm.cz/rozpusteny-a-vypusteny/
	Batman ---> https://www.ffdm.cz/batman/
	12 opic ---> https://www.ffdm.cz/12-opic/
	Slavnosti sněženek ---> https://www.ffdm.cz/slavnosti-snezenek/
	Dva papežové ---> https://www.ffdm.cz/dva-papezove/
	Pátrání po Sugar Manovi ---> https://www.ffdm.cz/patrani-po-sugar-manovi/
Workshopy a soutěže
	Programovací workshop ---> https://www.ffdm.cz/programovaci-workshop/
	Why man creates ---> https://www.ffdm.cz/why-man-creates/
	MEME soutěž ---> https://www.ffdm.cz/meme-soutez/
Duchovní programy
	Kdo to vůbec je? ---> link chybi
Další tipy
	Mapathon s Missing Maps ---> https://www.ffdm.cz/mapathon-s-missing-maps/
	NEW: Zrní je hra ---> https://www.ffdm.cz/new-zrni-je-hra/
	NEW: Masterclass: Ventolin ---> https://www.ffdm.cz/new-masterclass-ventolin/
	NEW: Amelie Siba – Dye my hair ---> https://www.ffdm.cz/amelie-siba-dye-my-hair/
	NEW: Czech Space Week 2020 ---> https://www.ffdm.cz/czech-space-week-2020/
	Matěj Ptaszek na rádiu Beat ---> https://www.ffdm.cz/matej-ptaszek-na-radiu-beat/
	Matt Berninger – Serpentine Prison ---> https://www.ffdm.cz/matt-berninger-serpentine-prison/
	Hadag Nahash – korona koncert ---> https://www.ffdm.cz/hadag-nahash-korona-koncert/
	Člověk krve – V kuchyni ---> https://www.ffdm.cz/clovek-krve-v-kuchyni/
Tipy účastníků
```


# TODO
- použít regulární výrazy na najití datumů
- přidat testy ;-)
- přidat barvičky do výstup? S barvami je vždycky všechno lepší.
- zdokumentovat/okomentovat aplikaci
