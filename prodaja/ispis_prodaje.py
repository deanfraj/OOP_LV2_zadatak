from korisnik import ispis_korisnika
from artikl import ispis_artikla
def ispis_prodaje(prodaja):

    print("Informacije o korisniku:")
    ispis_korisnika(prodaja['korisnik'])
    print("Informacije o artiklu:")
    ispis_artikla(prodaja['artikl'])
    print("Datum isteka:")
    print(f"\t Dan: {prodaja['datum'].day}")
    print(f"\t Mjesec: {prodaja['datum'].month}")
    print(f"\t Godina: {prodaja['datum'].year}")
