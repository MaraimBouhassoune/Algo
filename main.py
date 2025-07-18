from utilitaires import lire_csv_biens
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide

if __name__ == "__main__":
    chemin_csv = "transactions_immobilieres.csv"
    tailles = [100, 500, 1000]
    criteres = [
        ("prix", "PRIX"),
        ("surface", "SURFACE")
    ]
    tris = [
        (tri_selection, "SÉLECTION"),
        (tri_insertion, "INSERTION"),
        (tri_fusion, "FUSION"),
        (tri_rapide, "RAPIDE")
    ]

    lignes_resultats = []

    for taille in tailles:
        for cle, nom_critere in criteres:
            if cle == "prix":
                titre = f"\n=== TRI PAR PRIX ({taille} éléments) ==="
            else:
                titre = f"\n=== TRI PAR SURFACE ({taille} éléments) ==="
            print(titre)
            lignes_resultats.append(titre)
            biens = lire_csv_biens(chemin_csv, nb_elements=taille)
            for tri_fct, nom_tri in tris:
                if nom_tri == "FUSION":
                    tab_trie, nb_comp, temps = tri_fct(biens, cle)
                    ligne = f"Tri {nom_tri} par {nom_critere} : {temps:.4f}s | {nb_comp} comparaisons"
                elif nom_tri == "INSERTION":
                    tab_trie, nb_comp, nb_decal, temps = tri_fct(biens, cle)
                    ligne = f"Tri {nom_tri} par {nom_critere} : {temps:.4f}s | {nb_comp} comparaisons | {nb_decal} décalages"
                else:
                    tab_trie, nb_comp, nb_ech, temps = tri_fct(biens, cle)
                    ligne = f"Tri {nom_tri} par {nom_critere} : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges"
                print(ligne)
                lignes_resultats.append(ligne)

    # Écriture dans le fichier resultats.txt
    with open("resultats.txt", "w", encoding="utf-8") as f:
        for ligne in lignes_resultats:
            f.write(ligne + "\n") 