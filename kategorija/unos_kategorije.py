from artikl import unos_artikla
def unos_kategorije(i):
    kategorija = {}
    kategorija['naziv'] = input(f"Unesite naziv {i + 1}. kategorije: ")

    artikli = []

    broj_artikala = int(input(f"Unesite broj artikala za {i + 1}. kategoriju: "))

    for i in range(broj_artikala):
        artikli.append(unos_artikla(i))
        kategorija['artikli'] = artikli

    return kategorija