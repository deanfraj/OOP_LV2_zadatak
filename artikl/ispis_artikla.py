def ispis_artikla(artikl):
    print(f"\t Naslov: {artikl['naslov']}")
    print(f"\t Opis: {artikl['opis']}")
    print(f"\t Cijena: {artikl['cijena']}")

def get_artikl(j, artikl):
    return f"\t{j}. {artikl['naslov']}"