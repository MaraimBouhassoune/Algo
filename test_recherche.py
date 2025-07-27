"""
test_recherche.py
Fichier de test pour vérifier immédiatement les algorithmes de recherche.
Utilise un mini-tableau fictif pour tester chaque fonction.
"""

from algorithmes_recherche import (
    recherche_lineaire, recherche_binaire, recherche_min_max,
    format_resultat_recherche_lineaire, format_resultat_recherche_binaire, format_resultat_min_max
)


biens_test = [
    {'prix': 200000, 'surface': 50, 'type_local': 'Appartement', 'commune': 'PARIS', 'nb_pieces': 2, 'prix_m2': 4000},
    {'prix': 350000, 'surface': 80, 'type_local': 'Maison', 'commune': 'PARIS', 'nb_pieces': 4, 'prix_m2': 4375},
    {'prix': 150000, 'surface': 30, 'type_local': 'Appartement', 'commune': 'LYON', 'nb_pieces': 1, 'prix_m2': 5000},
    {'prix': 450000, 'surface': 100, 'type_local': 'Maison', 'commune': 'MARSEILLE', 'nb_pieces': 5, 'prix_m2': 4500},
    {'prix': 300000, 'surface': 60, 'type_local': 'Appartement', 'commune': 'PARIS', 'nb_pieces': 3, 'prix_m2': 5000},
    {'prix': 180000, 'surface': 40, 'type_local': 'Appartement', 'commune': 'TOULOUSE', 'nb_pieces': 2, 'prix_m2': 4500},
    {'prix': 500000, 'surface': 120, 'type_local': 'Maison', 'commune': 'BORDEAUX', 'nb_pieces': 6, 'prix_m2': 4167},
    {'prix': 250000, 'surface': 55, 'type_local': 'Appartement', 'commune': 'NANTES', 'nb_pieces': 3, 'prix_m2': 4545},
    {'prix': 400000, 'surface': 90, 'type_local': 'Maison', 'commune': 'PARIS', 'nb_pieces': 5, 'prix_m2': 4444},
    {'prix': 120000, 'surface': 25, 'type_local': 'Appartement', 'commune': 'LILLE', 'nb_pieces': 1, 'prix_m2': 4800}
]


biens_tries_prix = sorted(biens_test, key=lambda x: x['prix'])



def tester_recherche_lineaire_maisons_paris():
    """Test : Recherche de toutes les maisons à Paris"""
    print("=== Test Recherche Linéaire : Maisons à Paris ===")
    nb_trouves, nb_comp, temps = recherche_lineaire(
        biens_test,
        lambda x: x['type_local'] == 'Maison' and x['commune'] == 'PARIS'
    )
    resultat = format_resultat_recherche_lineaire(temps, nb_comp, nb_trouves)
    print(f"Recherche linéaire MAISONS PARIS : {temps:.4f}s | {nb_comp} comparaisons | Trouvées: {nb_trouves}")
    return resultat

def tester_recherche_lineaire_appart_3p():
    """Test : Recherche de tous les appartements 3 pièces"""
    print("=== Test Recherche Linéaire : Appartements 3 pièces ===")
    nb_trouves, nb_comp, temps = recherche_lineaire(
        biens_test,
        lambda x: x['type_local'] == 'Appartement' and x['nb_pieces'] == 3
    )
    resultat = format_resultat_recherche_lineaire(temps, nb_comp, nb_trouves)
    print(f"Recherche APPART 3P : {temps:.4f}s | {nb_comp} comparaisons | Trouvés: {nb_trouves}")
    return resultat

def tester_recherche_binaire_prix():
    """Test : Recherche binaire du prix 350000€"""
    print("=== Test Recherche Binaire : Prix 350000€ ===")
    pos, nb_comp, temps = recherche_binaire(
        biens_tries_prix,
        350000,
        'prix'
    )
    resultat = format_resultat_recherche_binaire(temps, nb_comp, pos)
    print(f"Recherche binaire PRIX 350000€ : {temps:.4f}s | {nb_comp} comparaisons | Position: {pos}")
    return resultat

def tester_recherche_min_max_prix_m2():
    """Test : Recherche min/max des prix au m²"""
    print("=== Test Recherche Min/Max : Prix au m² ===")
    vmin, vmax, nb_comp, temps = recherche_min_max(
        biens_test,
        'prix_m2'
    )
    resultat = format_resultat_min_max(temps, nb_comp, vmin, vmax)
    print(f"Min/Max PRIX_M2 : {temps:.4f}s | {nb_comp} comparaisons | Min: {vmin}€/m² | Max: {vmax}€/m²")
    return resultat



def lancer_tous_les_tests():
    """Lance tous les tests et sauvegarde les résultats"""
    print("🚀 LANCEMENT DES TESTS DE RECHERCHE")
    print("=" * 50)
    
    resultats = []
    
    
    resultat1 = tester_recherche_lineaire_maisons_paris()
    resultats.append(resultat1)
    print()
   
   
    resultat2 = tester_recherche_lineaire_appart_3p()
    resultats.append(resultat2)
    print()
    
   
    resultat3 = tester_recherche_binaire_prix()
    resultats.append(resultat3)
    print()
    
    
    resultat4 = tester_recherche_min_max_prix_m2()
    resultats.append(resultat4)
    print()
    
   
    sauvegarder_resultats(resultats)
    
    print("✅ Tests terminés ! Résultats sauvegardés dans resultats.txt")
    return resultats

def sauvegarder_resultats(resultats):
    """Sauvegarde les résultats dans resultats.txt"""
    with open('resultats.txt', 'w', encoding='utf-8') as f:
        f.write("=== RÉSULTATS DES TESTS DE RECHERCHE ===\n")
        f.write("Données de test : 10 biens fictifs\n\n")
        for i, resultat in enumerate(resultats, 1):
            f.write(f"Test {i} : {resultat}\n")
        f.write("\n=== FIN DES RÉSULTATS ===\n")



if __name__ == "__main__":
    lancer_tous_les_tests() 