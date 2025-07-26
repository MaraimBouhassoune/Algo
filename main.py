from utilitaires import lire_csv_biens
from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max

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

    # =========================
    # PARTIE 1 : TESTS DES TRIS
    # =========================
    print("🚀 TESTS DES ALGORITHMES DE TRI")
    print("=" * 50)

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

    # =========================
    # PARTIE 2 : TESTS DES RECHERCHES
    # =========================
    print("\n🔍 TESTS DES ALGORITHMES DE RECHERCHE")
    print("=" * 50)

    # Tests sur 500 éléments
    print("\n--- Tests sur 500 éléments ---")
    biens_500 = lire_csv_biens(chemin_csv, nb_elements=500)
    biens_500_tries_prix = tri_fusion(biens_500, "prix")[0]  # Utilise le tri fusion pour trier par prix

    # Test A : Recherche de TOUTES les Maisons à Paris (500 éléments)
    nb_trouves, nb_comp, temps = recherche_lineaire(
        biens_500,
        lambda x: x['type_local'] == 'Maison' and x['commune'] == 'PARIS'
    )
    ligne = f"Recherche linéaire MAISONS PARIS (500) : {temps:.4f}s | {nb_comp} comparaisons | Trouvées: {nb_trouves}"
    print(ligne)
    lignes_resultats.append(ligne)

    # Test B : Recherche Binaire d'un Prix Cible (500 éléments)
    pos, nb_comp, temps = recherche_binaire(
        biens_500_tries_prix,
        350000,
        'prix'
    )
    ligne = f"Recherche binaire PRIX 350000€ (500) : {temps:.4f}s | {nb_comp} comparaisons | Position: {pos}"
    print(ligne)
    lignes_resultats.append(ligne)

    # Test C : Recherche Min/Max des Prix au m² (500 éléments)
    vmin, vmax, nb_comp, temps = recherche_min_max(
        biens_500,
        'prix_m2'
    )
    ligne = f"Min/Max PRIX_M2 (500) : {temps:.4f}s | {nb_comp} comparaisons | Min: {vmin}€/m² | Max: {vmax}€/m²"
    print(ligne)
    lignes_resultats.append(ligne)

    # Test D : Recherche de TOUS les Appartements 3 Pièces (500 éléments)
    nb_trouves, nb_comp, temps = recherche_lineaire(
        biens_500,
        lambda x: x['type_local'] == 'Appartement' and x['nb_pieces'] == '3'
    )
    ligne = f"Recherche APPART 3P (500) : {temps:.4f}s | {nb_comp} comparaisons | Trouvés: {nb_trouves}"
    print(ligne)
    lignes_resultats.append(ligne)

    # Tests sur 1000 éléments
    print("\n--- Tests sur 1000 éléments ---")
    biens_1000 = lire_csv_biens(chemin_csv, nb_elements=1000)
    biens_1000_tries_prix = tri_fusion(biens_1000, "prix")[0]  # Utilise le tri fusion pour trier par prix

    # Test A : Recherche de TOUTES les Maisons à Paris (1000 éléments)
    nb_trouves, nb_comp, temps = recherche_lineaire(
        biens_1000,
        lambda x: x['type_local'] == 'Maison' and x['commune'] == 'PARIS'
    )
    ligne = f"Recherche linéaire MAISONS PARIS (1000) : {temps:.4f}s | {nb_comp} comparaisons | Trouvées: {nb_trouves}"
    print(ligne)
    lignes_resultats.append(ligne)

    # Test B : Recherche Binaire d'un Prix Cible (1000 éléments)
    pos, nb_comp, temps = recherche_binaire(
        biens_1000_tries_prix,
        350000,
        'prix'
    )
    ligne = f"Recherche binaire PRIX 350000€ (1000) : {temps:.4f}s | {nb_comp} comparaisons | Position: {pos}"
    print(ligne)
    lignes_resultats.append(ligne)

    # Test C : Recherche Min/Max des Prix au m² (1000 éléments)
    vmin, vmax, nb_comp, temps = recherche_min_max(
        biens_1000,
        'prix_m2'
    )
    ligne = f"Min/Max PRIX_M2 (1000) : {temps:.4f}s | {nb_comp} comparaisons | Min: {vmin}€/m² | Max: {vmax}€/m²"
    print(ligne)
    lignes_resultats.append(ligne)

    # Test D : Recherche de TOUS les Appartements 3 Pièces (1000 éléments)
    nb_trouves, nb_comp, temps = recherche_lineaire(
        biens_1000,
        lambda x: x['type_local'] == 'Appartement' and x['nb_pieces'] == '3'
    )
    ligne = f"Recherche APPART 3P (1000) : {temps:.4f}s | {nb_comp} comparaisons | Trouvés: {nb_trouves}"
    print(ligne)
    lignes_resultats.append(ligne)

    # =========================
    # SAUVEGARDE DES RÉSULTATS
    # =========================
    print("\n✅ Tous les tests terminés ! Sauvegarde des résultats...")
    
    # Écriture dans le fichier resultats.txt
    with open("resultats.txt", "w", encoding="utf-8") as f:
        f.write("=== RÉSULTATS COMPLETS : TRIS ET RECHERCHES ===\n\n")
        for ligne in lignes_resultats:
            f.write(ligne + "\n")
        f.write("\n=== FIN DES RÉSULTATS ===\n")
    
    print("📁 Résultats sauvegardés dans resultats.txt")
    print("📝 Prêt pour l'analyse dans analyse.txt") 