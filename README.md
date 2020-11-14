# O repozitáři
V tomto repozitáři je ukázková aplikace pro (Programovací workshop #1)[https://www.ffdm.cz/programovaci-workshop/] v rámci XVI. FFDM.

# O aplikaci

Cílem této aplikace je posbírat (angl. scrape) informace z webu FFDM https://www.ffdm.cz a zobrazit je uživateli.
Když tedy účastník FFDM bude chtít vědět, co se právě děje, tak stačí v terminálu pustit příkaz:

```bash
$ python ffdm-aktualne
FFDM Program:
Streamy:
    - Warm Up Stream
    - XVI. FFDM Stream
    - Bohoslužba
Workshopy:
    - ...
[...]
```

Aplikace se neklade za cíl být dokonalou, ale spíš ukázkovou toho, co je možné.

# TODO
- použít regulární výrazy na najití datumů
