
"""
Lecture « maison » du CSV : renvoie une liste de dictionnaires.
Aucune bibliothèque externe.
"""

def lire_csv_biens(path, n_max=None):
    biens = []
    with open(path, encoding="utf-8") as f:
        lignes = f.readlines()

    if not lignes:
        return biens

    header = lignes[0].strip().split(',')
    for line in lignes[1:]:
        if n_max is not None and len(biens) >= n_max:
            break
        vals = line.strip().split(',')
        if len(vals) != len(header):
            continue
        biens.append(dict(zip(header, vals)))
    return biens
