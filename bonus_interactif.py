"""
🏆 BONUS INTERACTIF - ANALYSE DE PERFORMANCE AVANCÉE
Interface utilisateur complète avec fonctionnalités avancées
"""

from utilitaires import lire_csv_biens
from algorithmes_tri import (
    tri_selection, tri_insertion, tri_fusion, tri_rapide, tri_tas,
    comparer_tous_algorithmes_avec_bonus, valider_tri
)
from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max
import time
import random

def afficher_menu_principal():
    """Affiche le menu principal du bonus interactif"""
    print("\n" + "="*70)
    print("🏆 BONUS INTERACTIF - ANALYSE DE PERFORMANCE AVANCÉE")
    print("="*70)
    print("1. 🏁 Comparaison complète (5 algorithmes incluant le bonus)")
    print("2. 🔍 Test détaillé du tri par tas (Heap Sort)")
    print("3. 📊 Benchmark avec statistiques avancées")
    print("4. 🎲 Test sur données aléatoires générées")
    print("5. 📈 Analyse de complexité théorique vs pratique")
    print("6. 🏠 Tests sur données immobilières spécifiques")
    print("7. 🎯 Mode compétition (classement des algorithmes)")
    print("8. 🔬 Analyse de stabilité des algorithmes")
    print("9. 📋 Rapport de performance complet")
    print("0. ❌ Quitter")
    print("="*70)

def comparaison_complete_avec_bonus():
    """Compare tous les algorithmes incluant le tri par tas"""
    print("\n🏁 COMPARAISON COMPLÈTE AVEC BONUS")
    print("="*60)
    
    chemin_csv = "transactions_immobilieres.csv"
    tailles = [100, 500, 1000]
    
    for taille in tailles:
        print(f"\n--- Tests sur {taille} éléments ---")
        biens = lire_csv_biens(chemin_csv, n_max=taille)
        
        # Tests par prix
        print(f"\n📈 TRI PAR PRIX ({taille} éléments):")
        comparer_tous_algorithmes_avec_bonus(biens, "prix")
        
        # Tests par surface
        print(f"\n📐 TRI PAR SURFACE ({taille} éléments):")
        comparer_tous_algorithmes_avec_bonus(biens, "surface")

def test_detaille_tri_tas():
    """Test spécifique du tri par tas avec explications détaillées"""
    print("\n🔍 TEST DÉTAILLÉ DU TRI PAR TAS (HEAP SORT)")
    print("="*60)
    
    chemin_csv = "transactions_immobilieres.csv"
    biens = lire_csv_biens(chemin_csv, n_max=100)
    
    print("📋 Principe du tri par tas :")
    print("  1. 🏗️  Construction du tas max à partir du tableau")
    print("  2. 🔄 Extraction du maximum (racine) et placement à la fin")
    print("  3. 🔧 Réorganisation du tas et répétition")
    print("  4. ✅ Complexité garantie O(n log n) dans tous les cas")
    print("  5. 💾 Avantage : tri in-place (pas de mémoire supplémentaire)")
    
    print(f"\n🧪 Test sur {len(biens)} éléments :")
    
    # Test par prix
    tab_trie, nb_comp, nb_ech, temps = tri_tas(biens, "prix")
    print(f"  💰 Prix  : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    # Test par surface
    tab_trie, nb_comp, nb_ech, temps = tri_tas(biens, "surface")
    print(f"  📐 Surface : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    # Validation
    valide, msg = valider_tri(biens, tab_trie, "prix")
    print(f"\n✅ Vérification : {msg}")
    print(f"   Premier prix : {tab_trie[0]['prix']}€")
    print(f"   Dernier prix : {tab_trie[-1]['prix']}€")

def benchmark_statistiques_avancees():
    """Benchmark complet avec statistiques avancées"""
    print("\n📊 BENCHMARK AVEC STATISTIQUES AVANCÉES")
    print("="*60)
    
    chemin_csv = "transactions_immobilieres.csv"
    tailles = [100, 500, 1000]
    algorithmes = [
        ("Sélection", tri_selection),
        ("Insertion", tri_insertion),
        ("Fusion", tri_fusion),
        ("Rapide", tri_rapide),
        ("🏆 TAS (BONUS)", tri_tas)
    ]
    
    print(f"{'Taille':<8} {'Algorithme':<15} {'Temps (s)':<10} {'Comparaisons':<12} {'Opérations':<12} {'Vitesse':<10}")
    print("-" * 80)
    
    for taille in tailles:
        biens = lire_csv_biens(chemin_csv, n_max=taille)
        print(f"\n{taille:>4} éléments:")
        
        temps_min = float('inf')
        resultats = []
        
        for nom, algo in algorithmes:
            if nom == "Fusion":
                tab_trie, nb_comp, temps = algo(biens, "prix")
                nb_op = nb_comp
            else:
                tab_trie, nb_comp, nb_op, temps = algo(biens, "prix")
            
            resultats.append((nom, temps, nb_comp, nb_op))
            if temps < temps_min:
                temps_min = temps
        
        # Affichage avec indicateur de vitesse
        for nom, temps, nb_comp, nb_op in resultats:
            vitesse = temps_min / temps if temps > 0 else 1
            indicateur = "🏆" if vitesse >= 0.9 else "🥈" if vitesse >= 0.5 else "🥉" if vitesse >= 0.1 else "🐌"
            print(f"{'':>8} {nom:<15} {temps:<10.4f} {nb_comp:<12} {nb_op:<12} {indicateur}")

def test_donnees_aleatoires():
    """Test sur des données aléatoires pour démontrer la robustesse"""
    print("\n🎲 TEST SUR DONNÉES ALÉATOIRES")
    print("="*50)
    
    # Générer des données aléatoires réalistes
    donnees_aleatoires = []
    types_biens = ['Appartement', 'Maison', 'Studio', 'Loft']
    communes = ['PARIS', 'LYON', 'MARSEILLE', 'BORDEAUX', 'TOULOUSE', 'NICE']
    
    for i in range(100):
        donnees_aleatoires.append({
            'prix': str(random.randint(80000, 1500000)),
            'surface': str(random.randint(15, 300)),
            'type_local': random.choice(types_biens),
            'commune': random.choice(communes),
            'nb_pieces': str(random.randint(1, 10)),
            'prix_m2': str(random.randint(1500, 20000))
        })
    
    print(f"🧪 Test sur {len(donnees_aleatoires)} données aléatoires :")
    
    # Test du tri par tas
    tab_trie, nb_comp, nb_ech, temps = tri_tas(donnees_aleatoires, "prix")
    print(f"  🏆 Tri par tas : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
    
    # Vérification
    prix_tries = [int(x['prix']) for x in tab_trie]
    est_trie = prix_tries == sorted(prix_tries)
    print(f"  ✅ Vérification tri : {'CORRECT' if est_trie else 'ERREUR'}")
    
    # Statistiques
    print(f"  📊 Prix min : {prix_tries[0]:,}€")
    print(f"  📊 Prix max : {prix_tries[-1]:,}€")
    print(f"  📊 Prix médian : {prix_tries[len(prix_tries)//2]:,}€")

def analyse_complexite_theorique_pratique():
    """Analyse théorique vs pratique de la complexité"""
    print("\n📈 ANALYSE DE COMPLEXITÉ THÉORIQUE VS PRATIQUE")
    print("="*65)
    
    print("📚 Complexité théorique :")
    print("  • Tri Sélection : O(n²) - toujours")
    print("  • Tri Insertion : O(n²) - moyen cas")
    print("  • Tri Fusion    : O(n log n) - toujours")
    print("  • Tri Rapide    : O(n log n) - moyen cas, O(n²) - pire cas")
    print("  • 🏆 Tri par Tas : O(n log n) - toujours (GARANTI)")
    
    print("\n🔬 Analyse pratique sur nos données :")
    chemin_csv = "transactions_immobilieres.csv"
    tailles = [100, 500, 1000]
    
    for taille in tailles:
        biens = lire_csv_biens(chemin_csv, n_max=taille)
        print(f"\n  {taille} éléments :")
        
        # Tri par tas
        tab_trie, nb_comp, nb_ech, temps = tri_tas(biens, "prix")
        theorique = taille * (taille ** 0.5)  # Approximation O(n log n)
        ratio = nb_comp / theorique if theorique > 0 else 0
        print(f"    🏆 Tri par tas : {nb_comp} comp (théorique ~{theorique:.0f}, ratio: {ratio:.2f})")
        
        # Tri fusion pour comparaison
        tab_trie, nb_comp, temps = tri_fusion(biens, "prix")
        ratio = nb_comp / theorique if theorique > 0 else 0
        print(f"    🔄 Tri fusion : {nb_comp} comp (ratio: {ratio:.2f})")

def tests_donnees_specifiques():
    """Test sur des données immobilières spécifiques"""
    print("\n🏠 TESTS SUR DONNÉES IMMOBILIÈRES SPÉCIFIQUES")
    print("="*60)
    
    chemin_csv = "transactions_immobilieres.csv"
    biens = lire_csv_biens(chemin_csv, n_max=200)
    
    # Filtrer les maisons à Paris
    maisons_paris = [b for b in biens if b['type_local'] == 'Maison' and b['commune'] == 'PARIS']
    print(f"🏠 Maisons à Paris trouvées : {len(maisons_paris)}")
    
    if maisons_paris:
        print("\n📊 Tri des maisons parisiennes par prix (tri par tas) :")
        tab_trie, nb_comp, nb_ech, temps = tri_tas(maisons_paris, "prix")
        print(f"  Temps : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
        
        print("\n🏆 Top 5 des maisons les plus chères à Paris :")
        for i, maison in enumerate(tab_trie[-5:], 1):
            print(f"  {i}. {maison['prix']}€ - {maison['surface']}m² - {maison['nb_pieces']} pièces")
    
    # Filtrer les appartements de luxe (> 800k€)
    appart_luxe = [b for b in biens if b['type_local'] == 'Appartement' and int(b['prix']) > 800000]
    print(f"\n🏢 Appartements de luxe (>800k€) trouvés : {len(appart_luxe)}")
    
    if appart_luxe:
        print("\n📊 Tri des appartements de luxe par prix au m² :")
        tab_trie, nb_comp, nb_ech, temps = tri_tas(appart_luxe, "prix_m2")
        print(f"  Temps : {temps:.4f}s | {nb_comp} comparaisons | {nb_ech} échanges")
        
        print("\n💎 Top 3 des appartements les plus chers au m² :")
        for i, appart in enumerate(tab_trie[-3:], 1):
            print(f"  {i}. {appart['prix_m2']}€/m² - {appart['prix']}€ - {appart['surface']}m²")

def mode_competition():
    """Mode compétition - classement des algorithmes"""
    print("\n🎯 MODE COMPÉTITION - CLASSEMENT DES ALGORITHMES")
    print("="*65)
    
    chemin_csv = "transactions_immobilieres.csv"
    biens = lire_csv_biens(chemin_csv, n_max=500)
    
    algorithmes = [
        ("Sélection", tri_selection),
        ("Insertion", tri_insertion),
        ("Fusion", tri_fusion),
        ("Rapide", tri_rapide),
        ("🏆 TAS (BONUS)", tri_tas)
    ]
    
    resultats = []
    
    print("🏁 Course des algorithmes sur 500 éléments...")
    for nom, algo in algorithmes:
        if nom == "Fusion":
            tab_trie, nb_comp, temps = algo(biens, "prix")
            resultats.append((nom, temps, nb_comp, 0))
        else:
            tab_trie, nb_comp, nb_op, temps = algo(biens, "prix")
            resultats.append((nom, temps, nb_comp, nb_op))
    
    # Classement par temps
    resultats_tries = sorted(resultats, key=lambda x: x[1])
    
    print("\n🏆 PODIUM FINAL :")
    print("="*40)
    for i, (nom, temps, comp, ops) in enumerate(resultats_tries, 1):
        medaille = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
        print(f"{medaille} {i}. {nom:<20} : {temps:.4f}s | {comp} comp")

def analyse_stabilite():
    """Analyse de la stabilité des algorithmes"""
    print("\n🔬 ANALYSE DE STABILITÉ DES ALGORITHMES")
    print("="*55)
    
    # Créer des données avec des valeurs identiques pour tester la stabilité
    donnees_test = [
        {'prix': '100000', 'id': 1, 'type': 'A'},
        {'prix': '100000', 'id': 2, 'type': 'B'},
        {'prix': '100000', 'id': 3, 'type': 'C'},
        {'prix': '200000', 'id': 4, 'type': 'D'},
        {'prix': '200000', 'id': 5, 'type': 'E'},
    ]
    
    print("📋 Test de stabilité sur données avec prix identiques :")
    print("   Données originales : A(100k) → B(100k) → C(100k) → D(200k) → E(200k)")
    
    algorithmes = [
        ("Insertion", tri_insertion),
        ("Fusion", tri_fusion),
        ("Rapide", tri_rapide),
        ("🏆 TAS", tri_tas)
    ]
    
    for nom, algo in algorithmes:
        if nom == "Fusion":
            trie, comp, temps = algo(donnees_test, "prix")
        else:
            trie, comp, ops, temps = algo(donnees_test, "prix")
        
        ordre_resultat = [item['type'] for item in trie]
        stable = ordre_resultat == ['A', 'B', 'C', 'D', 'E']
        statut = "✅ STABLE" if stable else "❌ INSTABLE"
        print(f"  {nom:<10} : {ordre_resultat} → {statut}")

def rapport_performance_complet():
    """Génère un rapport de performance complet"""
    print("\n📋 RAPPORT DE PERFORMANCE COMPLET")
    print("="*55)
    
    chemin_csv = "transactions_immobilieres.csv"
    biens = lire_csv_biens(chemin_csv, n_max=1000)
    
    print("📊 Résumé des performances sur 1000 éléments :")
    print("-" * 55)
    
    algorithmes = [
        ("Sélection", tri_selection),
        ("Insertion", tri_insertion),
        ("Fusion", tri_fusion),
        ("Rapide", tri_rapide),
        ("🏆 TAS (BONUS)", tri_tas)
    ]
    
    for nom, algo in algorithmes:
        if nom == "Fusion":
            tab_trie, nb_comp, temps = algo(biens, "prix")
            print(f"  {nom:<15} : {temps:.4f}s | {nb_comp:,} comparaisons")
        else:
            tab_trie, nb_comp, nb_op, temps = algo(biens, "prix")
            ops_nom = "décalages" if nom == "Insertion" else "échanges"
            print(f"  {nom:<15} : {temps:.4f}s | {nb_comp:,} comp | {nb_op:,} {ops_nom}")
    
    print("\n🏆 RECOMMANDATIONS :")
    print("  • 🥇 Tri Fusion : Meilleur pour la stabilité")
    print("  • 🥈 Tri Rapide : Meilleur pour la vitesse générale")
    print("  • 🥉 Tri par Tas : Meilleur pour la garantie de performance")
    print("  • 🐌 Tri Sélection : À éviter sur gros volumes")

def main():
    """Fonction principale du menu interactif"""
    print("🎉 Bienvenue dans le BONUS INTERACTIF !")
    
    while True:
        afficher_menu_principal()
        choix = input("\n🎯 Votre choix (0-9) : ").strip()
        
        if choix == "1":
            comparaison_complete_avec_bonus()
        elif choix == "2":
            test_detaille_tri_tas()
        elif choix == "3":
            benchmark_statistiques_avancees()
        elif choix == "4":
            test_donnees_aleatoires()
        elif choix == "5":
            analyse_complexite_theorique_pratique()
        elif choix == "6":
            tests_donnees_specifiques()
        elif choix == "7":
            mode_competition()
        elif choix == "8":
            analyse_stabilite()
        elif choix == "9":
            rapport_performance_complet()
        elif choix == "0":
            print("\n👋 Merci d'avoir testé le bonus interactif !")
            break
        else:
            print("❌ Choix invalide. Veuillez choisir entre 0 et 9.")
        
        input("\n⏸️  Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main() 