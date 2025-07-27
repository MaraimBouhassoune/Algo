"""
PROJET ALGORITHMIE - ANALYSE DE PERFORMANCE
============================================

Tests complets des algorithmes de tri et recherche selon le cahier des charges :
- 4 algorithmes de tri sur 2 critères × 3 tailles
- 3 algorithmes de recherche sur 3 tailles  
- Mesure temps + comptage opérations
- Génération d'un rapport complet

→ Génère resultats.txt avec toutes les mesures
→ Génère analyse_complete.txt avec l'analyse détaillée
"""

from utilitaires import lire_csv_biens, afficher_statistiques_dataset, valider_donnees
from algorithmes_tri import (
    tri_selection, tri_insertion, tri_fusion, tri_rapide,
    comparer_algorithmes_tri, valider_tri
)
from algorithmes_recherche import (
    recherche_lineaire, recherche_binaire, recherche_min_max,
    comparer_recherches, valider_recherche_binaire, analyser_repartition
)
from datetime import datetime
import os


# Configuration des tests
CSV_FILE = "transactions_immobilieres.csv"
TAILLES_TEST = [100, 500, 1000]
CRITERES_TRI = [("prix", "PRIX"), ("surface", "SURFACE")]
ALGORITHMES_TRI = [
    (tri_selection, "SÉLECTION"),
    (tri_insertion, "INSERTION"), 
    (tri_fusion, "FUSION"),
    (tri_rapide, "RAPIDE")
]


def executer_tests_tri(biens_base, taille, critere_key, critere_nom):
    """
    Exécute tous les tests de tri pour une taille et un critère donnés.
    """
    echantillon = biens_base[:taille]
    resultats = []
    
    print(f"\n=== TRI PAR {critere_nom} ({taille} éléments) ===")
    
    for algo_func, algo_nom in ALGORITHMES_TRI:
        try:
            if algo_nom == "FUSION":
                # Tri fusion retourne (liste, comparaisons, temps)
                trie, comparaisons, temps = algo_func(echantillon, critere_key)
                operations = 0  
                type_ops = ""
            else:
             
                trie, comparaisons, operations, temps = algo_func(echantillon, critere_key)
                type_ops = "décalages" if algo_nom == "INSERTION" else "échanges"
            
         
            valide, msg = valider_tri(echantillon, trie, critere_key)
            if not valide:
                print(f"❌ ERREUR - {algo_nom}: {msg}")
                continue
            
         
            if type_ops:
                print(f"Tri {algo_nom:<10} : {temps:>8.6f}s | {comparaisons:>6} comparaisons | {operations:>6} {type_ops}")
            else:
                print(f"Tri {algo_nom:<10} : {temps:>8.6f}s | {comparaisons:>6} comparaisons")
            
            resultats.append({
                'algorithme': algo_nom,
                'taille': taille,
                'critere': critere_nom,
                'temps': temps,
                'comparaisons': comparaisons,
                'operations': operations,
                'type_operations': type_ops,
                'valide': valide
            })
            
        except Exception as e:
            print(f"❌ ERREUR lors du tri {algo_nom}: {e}")
    
    return resultats


def executer_tests_recherche(biens_base, taille):
    """
    Exécute tous les tests de recherche pour une taille donnée.
    """
    echantillon = biens_base[:taille]
    resultats = []
    
    print(f"\n--- Tests de recherche sur {taille} éléments ---")
    
    try:
        
        biens_tries_prix, _, _ = tri_fusion(echantillon, "prix")
        
        # Test 1: Recherche linéaire - Maisons à Paris
        nb_maisons, comp_maisons, temps_maisons = recherche_lineaire(
            echantillon,
            lambda x: x.get("type_local") == "Maison" and x.get("commune") == "PARIS"
        )
        print(f"Recherche linéaire MAISONS PARIS ({taille:>4}) : {temps_maisons:>8.6f}s | {comp_maisons:>4} cmp | {nb_maisons:>2} trouvées")
        
        resultats.append({
            'type': 'Recherche linéaire',
            'cible': 'Maisons Paris',
            'taille': taille,
            'temps': temps_maisons,
            'comparaisons': comp_maisons,
            'resultats': nb_maisons
        })
        
        # Test 2: Recherche binaire - Prix 350000€
        pos_prix, comp_prix, temps_prix = recherche_binaire(biens_tries_prix, 350000, "prix")
        print(f"Recherche binaire 350000€ ({taille:>4})        : {temps_prix:>8.6f}s | {comp_prix:>4} cmp | pos {pos_prix}")
        
        resultats.append({
            'type': 'Recherche binaire',
            'cible': '350000€',
            'taille': taille,
            'temps': temps_prix,
            'comparaisons': comp_prix,
            'resultats': pos_prix
        })
        
        # Test 3: Min/Max - Prix au m²
        min_prix_m2, max_prix_m2, comp_minmax, temps_minmax = recherche_min_max(echantillon, "prix_m2")
        print(f"Min/Max PRIX_M2 ({taille:>4})               : {temps_minmax:>8.6f}s | {comp_minmax:>4} cmp | {min_prix_m2:.0f} – {max_prix_m2:.0f} €/m²")
        
        resultats.append({
            'type': 'Min/Max',
            'cible': 'Prix/m²',
            'taille': taille,
            'temps': temps_minmax,
            'comparaisons': comp_minmax,
            'resultats': f"{min_prix_m2:.0f}-{max_prix_m2:.0f}"
        })
        
        # Test 4: Recherche linéaire - Appartements 3 pièces
        nb_appart3p, comp_appart3p, temps_appart3p = recherche_lineaire(
            echantillon,
            lambda x: x.get("type_local") == "Appartement" and str(x.get("nb_pieces")) == "3"
        )
        print(f"Recherche APPART 3P ({taille:>4})            : {temps_appart3p:>8.6f}s | {comp_appart3p:>4} cmp | {nb_appart3p:>2} trouvés")
        
        resultats.append({
            'type': 'Recherche linéaire',
            'cible': 'Appartements 3P',
            'taille': taille,
            'temps': temps_appart3p,
            'comparaisons': comp_appart3p,
            'resultats': nb_appart3p
        })
        
    except Exception as e:
        print(f"❌ ERREUR lors des tests de recherche: {e}")
    
    return resultats


def generer_rapport_complet(resultats_tri, resultats_recherche, biens_originaux):
    """
    Génère un rapport d'analyse complet des résultats.
    """
    rapport = []
    
    
    rapport.append("=" * 80)
    rapport.append("RAPPORT D'ANALYSE DE PERFORMANCE - ALGORITHMES TRI & RECHERCHE")
    rapport.append("=" * 80)
    rapport.append(f"Généré le : {datetime.now().strftime('%d/%m/%Y à %H:%M:%S')}")
    rapport.append(f"Dataset : {len(biens_originaux)} biens immobiliers")
    rapport.append("")
    
   
    rapport.append("PARTIE 1 : ANALYSE DES ALGORITHMES DE TRI")
    rapport.append("-" * 50)
    rapport.append("")
    
    
    for taille in TAILLES_TEST:
        for critere_key, critere_nom in CRITERES_TRI:
            rapport.append(f"=== {critere_nom} - {taille} éléments ===")
            
            resultats_filtrés = [r for r in resultats_tri 
                               if r['taille'] == taille and r['critere'] == critere_nom]
            
            if resultats_filtrés:
                # Tri par temps pour le classement
                resultats_filtrés.sort(key=lambda x: x['temps'])
                
                for i, r in enumerate(resultats_filtrés, 1):
                    temps_ms = r['temps'] * 1000
                    if r['type_operations']:
                        rapport.append(f"{i}. {r['algorithme']:<10} : {temps_ms:>7.2f}ms | "
                                     f"{r['comparaisons']:>6} comp | {r['operations']:>6} {r['type_operations']}")
                    else:
                        rapport.append(f"{i}. {r['algorithme']:<10} : {temps_ms:>7.2f}ms | "
                                     f"{r['comparaisons']:>6} comp")
                
                
                plus_rapide = resultats_filtrés[0]
                plus_lent = resultats_filtrés[-1]
                facteur = plus_lent['temps'] / plus_rapide['temps'] if plus_rapide['temps'] > 0 else 0
                
                rapport.append(f"→ Plus rapide : {plus_rapide['algorithme']} ({plus_rapide['temps']*1000:.2f}ms)")
                rapport.append(f"→ Plus lent   : {plus_lent['algorithme']} ({plus_lent['temps']*1000:.2f}ms)")
                rapport.append(f"→ Facteur     : ×{facteur:.1f}")
                rapport.append("")
    
   
    rapport.append("ANALYSE DES COMPLEXITÉS")
    rapport.append("-" * 30)
    rapport.append("")
    
   
    resultats_1000 = [r for r in resultats_tri if r['taille'] == 1000]
    if resultats_1000:
        rapport.append("Performance sur 1000 éléments (moyenne prix + surface) :")
        
      
        moyennes = {}
        for r in resultats_1000:
            algo = r['algorithme']
            if algo not in moyennes:
                moyennes[algo] = {'temps': [], 'comparaisons': []}
            moyennes[algo]['temps'].append(r['temps'])
            moyennes[algo]['comparaisons'].append(r['comparaisons'])
        
        for algo, donnees in moyennes.items():
            temps_moy = sum(donnees['temps']) / len(donnees['temps'])
            comp_moy = sum(donnees['comparaisons']) / len(donnees['comparaisons'])
            rapport.append(f"• {algo:<10} : {temps_moy*1000:>6.1f}ms | {comp_moy:>7.0f} comparaisons")
        
        rapport.append("")
    
   
    rapport.append("PARTIE 2 : ANALYSE DES ALGORITHMES DE RECHERCHE")
    rapport.append("-" * 55)
    rapport.append("")
    
    for taille in TAILLES_TEST:
        rapport.append(f"=== {taille} éléments ===")
        
        resultats_rech_taille = [r for r in resultats_recherche if r['taille'] == taille]
        
        for r in resultats_rech_taille:
            temps_ms = r['temps'] * 1000
            rapport.append(f"{r['type']:<20} ({r['cible']:<15}) : {temps_ms:>6.2f}ms | "
                         f"{r['comparaisons']:>4} comp | {r['resultats']}")
        
        
        lineaire = next((r for r in resultats_rech_taille 
                        if r['type'] == 'Recherche linéaire' and '350000' not in r['cible']), None)
        binaire = next((r for r in resultats_rech_taille 
                       if r['type'] == 'Recherche binaire'), None)
        
        if lineaire and binaire:
            if binaire['comparaisons'] > 0:
                gain_comp = taille / binaire['comparaisons']
                rapport.append(f"→ Gain recherche binaire : ×{gain_comp:.0f} (comparaisons)")
        
        rapport.append("")
    
    
    rapport.append("PARTIE 3 : CONCLUSIONS ET RECOMMANDATIONS")
    rapport.append("-" * 45)
    rapport.append("")
    
    rapport.append("RECOMMANDATIONS POUR LES TRIS :")
    rapport.append("• Petits datasets (< 100) : Tri insertion (simple et efficace)")
    rapport.append("• Datasets moyens/grands   : Tri fusion (O(n log n) garanti, stable)")
    rapport.append("• Performance pure         : Tri rapide (en moyenne le plus rapide)")
    rapport.append("• Stabilité requise        : Tri fusion (préserve l'ordre des égaux)")
    rapport.append("")
    
    rapport.append("RECOMMANDATIONS POUR LES RECHERCHES :")
    rapport.append("• Recherche unique sur données triées : Recherche binaire")
    rapport.append("• Recherche multiple/filtrée          : Recherche linéaire")
    rapport.append("• Statistiques (min/max)               : Un seul parcours optimisé")
    rapport.append("• Application réelle                   : Index de base de données")
    rapport.append("")
    
    
    rapport.append("OBSERVATIONS SPÉCIFIQUES :")
    rapport.append(f"• Dataset contient {len(biens_originaux)} transactions immobilières")
    
     
    prix_valides = [b['prix'] for b in biens_originaux if isinstance(b.get('prix'), (int, float))]
    if prix_valides:
        prix_min, prix_max = min(prix_valides), max(prix_valides)
        rapport.append(f"• Prix : {prix_min:,}€ → {prix_max:,}€ (étendue: {prix_max-prix_min:,}€)")
    
    
    types_biens = {}
    for bien in biens_originaux:
        type_bien = bien.get('type_local', 'Inconnu')
        types_biens[type_bien] = types_biens.get(type_bien, 0) + 1
    
    rapport.append("• Répartition par type :")
    for type_bien, count in sorted(types_biens.items()):
        pourcentage = 100 * count / len(biens_originaux)
        rapport.append(f"  - {type_bien} : {count} ({pourcentage:.1f}%)")
    
    rapport.append("")
    rapport.append("=" * 80)
    rapport.append("FIN DU RAPPORT")
    rapport.append("=" * 80)
    
    return rapport


def main():
    """
    Fonction principale - Exécute tous les tests selon le cahier des charges.
    """
    print("🚀 PROJET ALGORITHMIE - ANALYSE DE PERFORMANCE")
    print("=" * 60)
    print(f"Fichier source : {CSV_FILE}")
    
    
    if not os.path.exists(CSV_FILE):
        print(f"❌ ERREUR : Le fichier {CSV_FILE} n'existe pas !")
        print("   Veuillez vous assurer que le fichier CSV est dans le même dossier.")
        return
    
 
    # Chargement des données
    print("\n📂 CHARGEMENT DES DONNÉES")
    print("-" * 30)
    biens_complets = lire_csv_biens(CSV_FILE)
    
    if not biens_complets:
        print("❌ Aucune donnée chargée ! Vérifiez le fichier CSV.")
        return
    
     
    afficher_statistiques_dataset(biens_complets)
    
 
    if not valider_donnees(biens_complets):
        print("⚠️  Des erreurs ont été détectées, mais les tests continuent...")
    
     
    tous_resultats_tri = []
    tous_resultats_recherche = []
    logs_execution = []
    
    # PHASE 1 : Tests des algorithmes de tri
    print("\n🔄 PHASE 1 : TESTS DES ALGORITHMES DE TRI")
    print("=" * 50)
    
    for taille in TAILLES_TEST:
        for critere_key, critere_nom in CRITERES_TRI:
            resultats = executer_tests_tri(biens_complets, taille, critere_key, critere_nom)
            tous_resultats_tri.extend(resultats)
    
    # PHASE 2 : Tests des algorithmes de recherche  
    print("\n🔍 PHASE 2 : TESTS DES ALGORITHMES DE RECHERCHE")
    print("=" * 50)
    
    for taille in TAILLES_TEST:
        resultats = executer_tests_recherche(biens_complets, taille)
        tous_resultats_recherche.extend(resultats)
    
    # PHASE 3 : Génération des rapports
    print("\n📊 PHASE 3 : GÉNÉRATION DES RAPPORTS")
    print("=" * 40)
    
     
    try:
        with open("resultats.txt", "w", encoding="utf-8") as f:
            f.write("=== RÉSULTATS COMPLETS : TRIS & RECHERCHES ===\n\n")
            f.write("🚀 TESTS DES ALGORITHMES DE TRI\n")
            f.write("=" * 50 + "\n\n")
            
             
            for taille in TAILLES_TEST:
                for critere_key, critere_nom in CRITERES_TRI:
                    f.write(f"=== TRI PAR {critere_nom} ({taille} éléments) ===\n")
                    
                    resultats_filtres = [r for r in tous_resultats_tri 
                                       if r['taille'] == taille and r['critere'] == critere_nom]
                    
                    for r in resultats_filtres:
                        if r['type_operations']:
                            f.write(f"Tri {r['algorithme']} : {r['temps']:.6f}s | "
                                   f"{r['comparaisons']} comparaisons | "
                                   f"{r['operations']} {r['type_operations']}\n")
                        else:
                            f.write(f"Tri {r['algorithme']} : {r['temps']:.6f}s | "
                                   f"{r['comparaisons']} comparaisons\n")
                    f.write("\n")
            
            f.write("🔍 TESTS DES ALGORITHMES DE RECHERCHE\n")
            f.write("=" * 50 + "\n\n")
            
            for taille in TAILLES_TEST:
                f.write(f"--- Tests sur {taille} éléments ---\n")
                
                resultats_rech = [r for r in tous_resultats_recherche if r['taille'] == taille]
                for r in resultats_rech:
                    if r['type'] == 'Recherche linéaire' and 'Maisons' in r['cible']:
                        f.write(f"Recherche linéaire MAISONS PARIS ({taille}) : {r['temps']:.6f}s | {r['comparaisons']} cmp | {r['resultats']} trouvées\n")
                    elif r['type'] == 'Recherche binaire':
                        f.write(f"Recherche binaire 350000€ ({taille}) : {r['temps']:.6f}s | {r['comparaisons']} cmp | pos {r['resultats']}\n")
                    elif r['type'] == 'Min/Max':
                        f.write(f"Min/Max PRIX_M2 ({taille}) : {r['temps']:.6f}s | {r['comparaisons']} cmp | {r['resultats']} €/m²\n")
                    elif r['type'] == 'Recherche linéaire' and 'Appartements' in r['cible']:
                        f.write(f"Recherche APPART 3P ({taille}) : {r['temps']:.6f}s | {r['comparaisons']} cmp | {r['resultats']} trouvés\n")
                f.write("\n")
            
            f.write("=== FIN DES RÉSULTATS ===\n")
        
        print("✅ resultats.txt généré")
        
    except Exception as e:
        print(f"❌ ERREUR lors de la génération de resultats.txt : {e}")
    
     
    try:
        rapport_complet = generer_rapport_complet(tous_resultats_tri, tous_resultats_recherche, biens_complets)
        
        with open("analyse_complete.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(rapport_complet))
        
        print("✅ analyse_complete.txt généré")
        
    except Exception as e:
        print(f"❌ ERREUR lors de la génération du rapport : {e}")
    
    
    print(f"\n🎯 RÉSUMÉ FINAL")
    print(f"   • {len(tous_resultats_tri)} tests de tri effectués")
    print(f"   • {len(tous_resultats_recherche)} tests de recherche effectués")
    print(f"   • Dataset : {len(biens_complets)} biens immobiliers")
    print(f"   • Fichiers générés : resultats.txt, analyse_complete.txt")
    print(f"\n✅ PROJET TERMINÉ AVEC SUCCÈS !")


if __name__ == "__main__":
    main()