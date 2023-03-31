from datetime import date

#print(korisnik['ime'],korisnik['prezime'],korisnik['telefon'],korisnik['email'])

# print("Informacije o artiklu: \n","Naslov: ",prodaja['artikl']['naslov'], "\nOpis: ",prodaja['artikl']['opis'],"\nCijena: ", prodaja['artikl']['cijena'])
# print("\nDatum isteka prodaje: \n","Dan: ",prodaja['datum'].day, "\nMjesec: ",prodaja['datum'].month,"\nGodina: ", prodaja['datum'].year)
# print("\nInformacije o korisniku: \n",prodaja['korisnik']['ime'], prodaja['korisnik']['prezime'],"\nTelefon: ",prodaja['korisnik']['telefon'],"\nEmail: ", prodaja['korisnik']['email'])

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input("Unesite broj korisnika: "))

for i in range(broj_korisnika):
    korisnik = {}
    korisnik['ime'] = input(f"Unesite ime {i+1}. korisnika: ").capitalize()
    korisnik['prezime'] = input(f"Unesite prezime {i+1}. korisnika: ").capitalize()
    korisnik['telefon'] = int(input(f"Unesite telefonski broj {i+1}. korisnika: "))
    korisnik['email'] = input(f"Unesite e-mail adresu {i+1}. korisnika: ").strip()

    korisnici.append(korisnik)

broj_kategorija = int(input("Unesite broj kategorija: "))

for i in range(broj_kategorija):
    kategorija = {}
    kategorija['naziv'] = input(f"Unesite naziv {i+1}. kategorije: ")

    artikli = []

    broj_artikala = int(input(f"Unesite broj artikala za {i + 1}. kategoriju: "))

    for i in range(broj_artikala):
        artikl = {}
        artikl['naslov'] = input(f"Unesite naslov {i+1}. artikla: ")
        artikl['opis'] = input(f"Unesite opis {i+1}. artikla: ")
        artikl['cijena'] = float(input(f"Unesite cijenu {i+1}. artikla: "))

        artikli.append(artikl)

        kategorija['artikli'] = artikli

    kategorije.append(kategorija)

broj_prodaja = int(input(f"Unesite broj prodaja: "))

for i in range(broj_prodaja):
    prodaja = {}
    dan = int(input(f"Unesite dan isteka {i+1}. prodaje: "))
    mjesec = int(input(f"Unesite mjesec isteka {i+1}. prodaje: "))
    godina = int(input(f"Unesite godinu isteka {i+1}. prodaje: "))
    prodaja['datum'] = date(godina, mjesec, dan)

    print(f"Odaberite korisnika {i+1}. prodaje: ")

    for j, korisnik in enumerate(korisnici, start=1):
        print(f"\t{j}. {korisnik['ime']} {korisnik['prezime']}")

    odabrani_korisnik = int(input("Odabrani korisnik: "))
    prodaja['korisnik'] = korisnici[odabrani_korisnik-1]

    print(f"Odaberite kategoriju {i+1}. prodaje: ")
    for j, kategorija in enumerate(kategorije, start=1):
        print(f"\t{j}. {kategorija['naziv']}")

    odabrana_kategorija = int(input("Odabrana kategorija: "))

    print(f"Odabarite artikl {i+1}. prodaje:")
    for j, artikl in enumerate(kategorije[odabrana_kategorija-1]['artikli'], start=1):
        print(f"\t{j}. {artikl['naslov']}")

    odabrani_artikl = int(input("Odabrani artikl: "))
    prodaja['artikl'] = kategorije[odabrana_kategorija-1]['artikli'][odabrani_artikl-1]

    prodaje.append(prodaja)

for i, prodaja in enumerate(prodaje, start=1):
    print("-----------------------------------------------")
    print(f"{i}. prodaja:")
    print("Informacije o korisniku:")
    print(f"\t Ime: {prodaja['korisnik']['ime']}")
    print(f"\t Prezime: {prodaja['korisnik']['prezime']}")
    print(f"\t Telefon: {prodaja['korisnik']['telefon']}")
    print(f"\t Email: {prodaja['korisnik']['email']}")
    print("Informacije o artiklu:")
    print(f"\t Naslov: {prodaja['artikl']['naslov']}")
    print(f"\t Opis: {prodaja['artikl']['opis']}")
    print(f"\t Cijena: {prodaja['artikl']['cijena']}")
    print("Datum isteka:")
    print(f"\t Dan: {prodaja['datum'].day}")
    print(f"\t Mjesec: {prodaja['datum'].month}")
    print(f"\t Godina: {prodaja['datum'].year}")
    print("-----------------------------------------------")

