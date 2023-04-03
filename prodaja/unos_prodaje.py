from datetime import date
from korisnik import get_korisnik
from artikl import get_artikl
from kategorija import get_kategorija
def unos_prodaje(korisnici, kategorije, i):
    prodaja = {}
    dan = int(input(f"Unesite dan isteka {i + 1}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i + 1}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i + 1}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f"Odaberite korisnika {i + 1}. prodaje: ")

    for j, korisnik in enumerate(korisnici, start=1):
        print(get_korisnik(j, korisnik))

    odabrani_korisnik = int(input("Odabrani korisnik: "))
    prodaja['korisnik'] = korisnici[odabrani_korisnik - 1]

    print(f"Odaberite kategoriju {i + 1}. prodaje: ")
    for j, kategorija in enumerate(kategorije, start=1):
        print(get_kategorija(j, kategorija))

    odabrana_kategorija = int(input("Odabrana kategorija: "))

    print(f"Odabarite artikl {i + 1}. prodaje:")
    for j, artikl in enumerate(kategorije[odabrana_kategorija - 1]['artikli'], start=1):
        print(get_artikl(j, artikl))

    odabrani_artikl = int(input("Odabrani artikl: "))
    prodaja['artikl'] = kategorije[odabrana_kategorija - 1]['artikli'][odabrani_artikl - 1]

    return prodaja