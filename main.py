from datetime import date

korisnik = {}
korisnik['ime'] = input("Unesite ime korisnika: ").capitalize()
korisnik['prezime'] = input("Unesite prezime korisnika: ").capitalize()
korisnik['telefon'] = int(input("Unesite telefonski broj korisnika: "))
korisnik['email'] = input("Unesite e-mail adresu korisnika: ").strip()

#print(korisnik['ime'],korisnik['prezime'],korisnik['telefon'],korisnik['email'])

artikl = {}
artikl['naslov'] = input("Unesite naslov artikla: ")
artikl['opis'] = input("Unesite opis artikla: ")
artikl['cijena'] = float(input("Unesite cijenu artikla: "))

prodaja = {}
prodaja['korisnik'] = korisnik
prodaja['artikl'] = artikl

dan = int(input("Unesite dan istekla prodaje: "))
mjesec = int(input("Unesite mjesec isteka prodaje: "))
godina = int(input("Unesite godinu isteka prodaje: "))
prodaja['datum'] = date(godina, mjesec, dan)

print("Informacije o artiklu: \n","Naslov: ",prodaja['artikl']['naslov'], "\nOpis: ",prodaja['artikl']['opis'],"\nCijena: ", prodaja['artikl']['cijena'])
print("\nDatum isteka prodaje: \n","Dan: ",prodaja['datum'].day, "\nMjesec: ",prodaja['datum'].month,"\nGodina: ", prodaja['datum'].year)
print("\nInformacije o korisniku: \n",prodaja['korisnik']['ime'], prodaja['korisnik']['prezime'],"\nTelefon: ",prodaja['korisnik']['telefon'],"\nEmail: ", prodaja['korisnik']['email'])