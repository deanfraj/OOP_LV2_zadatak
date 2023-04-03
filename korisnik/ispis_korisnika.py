def ispis_korisnika(korisnik):
    print(f"\t Ime: {korisnik['ime']}")
    print(f"\t Prezime: {korisnik['prezime']}")
    print(f"\t Telefon: {korisnik['telefon']}")
    print(f"\t Email: {korisnik['email']}")
def get_korisnik(j, korisnik):
    return f"\t{j}. {korisnik['ime']} {korisnik['prezime']}"