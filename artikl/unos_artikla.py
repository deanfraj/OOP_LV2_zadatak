def unos_artikla(i):
    artikl = {}
    artikl['naslov'] = input(f"Unesite naslov {i + 1}. artikla: ")
    artikl['opis'] = input(f"Unesite opis {i + 1}. artikla: ")
    artikl['cijena'] = float(input(f"Unesite cijenu {i + 1}. artikla: "))
    return artikl