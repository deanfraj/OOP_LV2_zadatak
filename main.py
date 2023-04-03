from korisnik import unos_korisnika
from kategorija import unos_kategorije
from prodaja import unos_prodaje, ispis_prodaje

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input("Unesite broj korisnika: "))

for i in range(broj_korisnika):
    korisnici.append(unos_korisnika(i))

broj_kategorija = int(input("Unesite broj kategorija: "))

for i in range(broj_kategorija):
    kategorije.append(unos_kategorije(i))

broj_prodaja = int(input(f"Unesite broj prodaja: "))

for i in range(broj_prodaja):
    prodaje.append(unos_prodaje(korisnici, kategorije, i))

for i, prodaja in enumerate(prodaje, start=1):
    print("-----------------------------------------------")
    print(f"{i}. prodaja:")
    ispis_prodaje(prodaja)
    print("-----------------------------------------------")

