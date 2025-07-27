
"""
Mini‑batterie de 10 biens fictifs
→ resultats_tests_fictifs.txt
"""

from algorithmes_recherche import (
    recherche_lineaire,
    recherche_binaire,
    recherche_min_max,
)

BIENS = [
    {"prix": 200000, "surface": 50,  "type_local": "Appartement", "commune": "PARIS",     "nb_pieces": 2, "prix_m2": 4000},
    {"prix": 350000, "surface": 80,  "type_local": "Maison",      "commune": "PARIS",     "nb_pieces": 4, "prix_m2": 4375},
    {"prix": 150000, "surface": 30,  "type_local": "Appartement", "commune": "LYON",      "nb_pieces": 1, "prix_m2": 5000},
    {"prix": 450000, "surface": 100, "type_local": "Maison",      "commune": "MARSEILLE", "nb_pieces": 5, "prix_m2": 4500},
    {"prix": 300000, "surface": 60,  "type_local": "Appartement", "commune": "PARIS",     "nb_pieces": 3, "prix_m2": 5000},
    {"prix": 180000, "surface": 40,  "type_local": "Appartement", "commune": "TOULOUSE",  "nb_pieces": 2, "prix_m2": 4500},
    {"prix": 500000, "surface": 120, "type_local": "Maison",      "commune": "BORDEAUX",  "nb_pieces": 6, "prix_m2": 4167},
    {"prix": 250000, "surface": 55,  "type_local": "Appartement", "commune": "NANTES",    "nb_pieces": 3, "prix_m2": 4545},
    {"prix": 400000, "surface": 90,  "type_local": "Maison",      "commune": "PARIS",     "nb_pieces": 5, "prix_m2": 4444},
    {"prix": 120000, "surface": 25,  "type_local": "Appartement", "commune": "LILLE",     "nb_pieces": 1, "prix_m2": 4800},
]

def main():
    lines = ["=== MINI‑TESTS RECHERCHE ==="]

    nb, cmp_, t = recherche_lineaire(BIENS, lambda x: x["type_local"] == "Maison" and x["commune"] == "PARIS")
    lines.append(f"Maisons PARIS : {t:.6f}s | {cmp_} cmp | {nb} trouvées")

    nb, cmp_, t = recherche_lineaire(BIENS, lambda x: x["type_local"] == "Appartement" and x["nb_pieces"] == 3)
    lines.append(f"Appart 3P     : {t:.6f}s | {cmp_} cmp | {nb} trouvés")

    pos, cmp_, t = recherche_binaire(sorted(BIENS, key=lambda x: x["prix"]), 350000, "prix")
    lines.append(f"Prix 350k€    : {t:.6f}s | {cmp_} cmp | pos {pos}")

    vmin, vmax, cmp_, t = recherche_min_max(BIENS, "prix_m2")
    lines.append(f"Min/Max m²    : {t:.6f}s | {cmp_} cmp | {vmin} – {vmax}")

    print("\n".join(lines))
    with open("resultats_tests_fictifs.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
