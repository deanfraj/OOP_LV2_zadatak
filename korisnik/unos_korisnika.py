def unos_korisnika(i):
    korisnik = {}
    korisnik['ime'] = input(f"Unesite ime {i + 1}. korisnika: ").capitalize()
    korisnik['prezime'] = input(f"Unesite prezime {i + 1}. korisnika: ").capitalize()
    korisnik['telefon'] = int(input(f"Unesite telefonski broj {i + 1}. korisnika: "))
    korisnik['email'] = input(f"Unesite e-mail adresu {i + 1}. korisnika: ").strip()
    return korisnik