
"""
24 tests réels : 4 tris × 2 critères × 3 tailles
                 4 recherches × 3 tailles
→ resultats.txt
"""

from utilitaires import lire_csv_biens
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import (
    recherche_lineaire,
    recherche_binaire,
    recherche_min_max,
)

CSV  = "transactions_immobilieres.csv"
TAILLES = [100, 500, 1000]
CRITS   = [("prix", "PRIX"), ("surface", "SURFACE")]
TRIS    = [
    (tri_selection, "SÉLECTION"),
    (tri_insertion, "INSERTION"),
    (tri_fusion,    "FUSION"),
    (tri_rapide,    "RAPIDE"),
]


def _log(buf, txt):
    print(txt)
    buf.append(txt)


def main():
    lignes = []
    _log(lignes, "🚀 TESTS DES ALGORITHMES DE TRI")
    _log(lignes, "=" * 50)

   
    for n in TAILLES:
        base = lire_csv_biens(CSV, n_max=n)
        for key, lbl in CRITS:
            _log(lignes, f"\n=== TRI PAR {lbl} ({n} éléments) ===")
            for fct, nom in TRIS:
                if nom == "FUSION":
                    _, cmp_, t = fct(base, key)
                    s = f"Tri {nom} : {t:.6f}s | {cmp_} comparaisons"
                elif nom == "INSERTION":
                    _, cmp_, dec, t = fct(base, key)
                    s = f"Tri {nom} : {t:.6f}s | {cmp_} comparaisons | {dec} décalages"
                else:
                    _, cmp_, ech, t = fct(base, key)
                    s = f"Tri {nom} : {t:.6f}s | {cmp_} comparaisons | {ech} échanges"
                _log(lignes, s)

    
    _log(lignes, "\n🔍 TESTS DES ALGORITHMES DE RECHERCHE")
    _log(lignes, "=" * 50)

    for n in TAILLES:
        _log(lignes, f"\n--- Tests sur {n} éléments ---")
        biens = lire_csv_biens(CSV, n_max=n)
        biens_prix = tri_fusion(biens, "prix")[0]

        
        nb, cmp_, t = recherche_lineaire(biens, lambda x: x["type_local"] == "Maison" and x["commune"] == "PARIS")
        _log(lignes, f"Recherche linéaire MAISONS PARIS ({n}) : {t:.6f}s | {cmp_} cmp | {nb} trouvées")

        
        pos, cmp_, t = recherche_binaire(biens_prix, 350000, "prix")
        _log(lignes, f"Recherche binaire 350000€ ({n}) : {t:.6f}s | {cmp_} cmp | pos {pos}")

      
        vmin, vmax, cmp_, t = recherche_min_max(biens, "prix_m2")
        _log(lignes, f"Min/Max PRIX_M2 ({n}) : {t:.6f}s | {cmp_} cmp | {vmin} – {vmax} €/m²")

        
        nb, cmp_, t = recherche_lineaire(biens, lambda x: x["type_local"] == "Appartement" and x["nb_pieces"] == "3")
        _log(lignes, f"Recherche APPART 3P ({n}) : {t:.6f}s | {cmp_} cmp | {nb} trouvés")

    
    with open("resultats.txt", "w", encoding="utf-8") as f:
        f.write("=== RÉSULTATS COMPLETS : TRIS & RECHERCHES ===\n\n")
        f.write("\n".join(lignes))
        f.write("\n\n=== FIN DES RÉSULTATS ===\n")

    print("\n✅ resultats.txt généré")


if __name__ == "__main__":
    main()
