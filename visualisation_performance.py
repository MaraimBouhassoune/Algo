"""
📊 VISUALISATION DES PERFORMANCES - BONUS
Génération de graphiques ASCII pour visualiser les performances
"""

from utilitaires import lire_csv_biens
from algorithmes_tri import (
    tri_selection, tri_insertion, tri_fusion, tri_rapide, tri_tas
)
import time

def generer_graphique_temps(tailles, resultats):
    """Génère un graphique ASCII des temps d'exécution"""
    print("\n📊 GRAPHIQUE DES TEMPS D'EXÉCUTION")
    print("=" * 60)
    
    algorithmes = ["Sélection", "Insertion", "Fusion", "Rapide", "🏆 TAS"]
    max_temps = max(max(temps) for temps in resultats.values())
    
    # Échelle pour l'affichage (max 50 caractères)
    echelle = 50 / max_temps if max_temps > 0 else 1
    
    print(f"{'Taille':<8} {'Sélection':<12} {'Insertion':<12} {'Fusion':<12} {'Rapide':<12} {'TAS':<12}")
    print("-" * 80)
    
    for i, taille in enumerate(tailles):
        ligne = f"{taille:<8}"
        for algo in algorithmes:
            temps = resultats[algo][i]
            barres = int(temps * echelle)
            barre = "█" * barres
            ligne += f"{barre:<12}"
        print(ligne)
    
    print(f"\nÉchelle : 1█ = {max_temps/50:.4f}s")

def generer_graphique_comparaisons(tailles, resultats):
    """Génère un graphique ASCII du nombre de comparaisons"""
    print("\n🔍 GRAPHIQUE DES COMPARAISONS")
    print("=" * 60)
    
    algorithmes = ["Sélection", "Insertion", "Fusion", "Rapide", "🏆 TAS"]
    max_comp = max(max(comp) for comp in resultats.values())
    
    # Échelle pour l'affichage
    echelle = 50 / max_comp if max_comp > 0 else 1
    
    print(f"{'Taille':<8} {'Sélection':<12} {'Insertion':<12} {'Fusion':<12} {'Rapide':<12} {'TAS':<12}")
    print("-" * 80)
    
    for i, taille in enumerate(tailles):
        ligne = f"{taille:<8}"
        for algo in algorithmes:
            comp = resultats[algo][i]
            barres = int(comp * echelle)
            barre = "▓" * barres
            ligne += f"{barre:<12}"
        print(ligne)
    
    print(f"\nÉchelle : 1▓ = {max_comp/50:,.0f} comparaisons")

def generer_tableau_comparatif():
    """Génère un tableau comparatif complet"""
    print("\n📋 TABLEAU COMPARATIF COMPLET")
    print("=" * 100)
    
    chemin_csv = "transactions_immobilieres.csv"
    tailles = [100, 500, 1000]
    
    # Collecter les données
    temps_data = {
        "Sélection": [],
        "Insertion": [],
        "Fusion": [],
        "Rapide": [],
        "🏆 TAS": []
    }
    
    comp_data = {
        "Sélection": [],
        "Insertion": [],
        "Fusion": [],
        "Rapide": [],
        "🏆 TAS": []
    }
    
    for taille in tailles:
        biens = lire_csv_biens(chemin_csv, n_max=taille)
        
        # Tri sélection
        _, comp, _, temps = tri_selection(biens, "prix")
        temps_data["Sélection"].append(temps)
        comp_data["Sélection"].append(comp)
        
        # Tri insertion
        _, comp, _, temps = tri_insertion(biens, "prix")
        temps_data["Insertion"].append(temps)
        comp_data["Insertion"].append(comp)
        
        # Tri fusion
        _, comp, temps = tri_fusion(biens, "prix")
        temps_data["Fusion"].append(temps)
        comp_data["Fusion"].append(comp)
        
        # Tri rapide
        _, comp, _, temps = tri_rapide(biens, "prix")
        temps_data["Rapide"].append(temps)
        comp_data["Rapide"].append(comp)
        
        # Tri par tas
        _, comp, _, temps = tri_tas(biens, "prix")
        temps_data["🏆 TAS"].append(temps)
        comp_data["🏆 TAS"].append(comp)
    
    # Afficher le tableau
    print(f"{'Algorithme':<15} {'100él':<12} {'500él':<12} {'1000él':<12} {'Moyenne':<12}")
    print("-" * 100)
    
    for algo in temps_data.keys():
        temps_moyen = sum(temps_data[algo]) / len(temps_data[algo])
        ligne = f"{algo:<15}"
        for temps in temps_data[algo]:
            ligne += f"{temps:<12.4f}"
        ligne += f"{temps_moyen:<12.4f}"
        print(ligne)
    
    return temps_data, comp_data

def generer_analyse_scalabilite():
    """Analyse de la scalabilité des algorithmes"""
    print("\n📈 ANALYSE DE SCALABILITÉ")
    print("=" * 50)
    
    chemin_csv = "transactions_immobilieres.csv"
    tailles = [100, 500, 1000]
    
    print("Facteur d'augmentation du temps (100→500→1000 éléments):")
    print("-" * 50)
    
    algorithmes = [
        ("Sélection", tri_selection),
        ("Insertion", tri_insertion),
        ("Fusion", tri_fusion),
        ("Rapide", tri_rapide),
        ("🏆 TAS", tri_tas)
    ]
    
    for nom, algo in algorithmes:
        temps_100 = 0
        temps_500 = 0
        temps_1000 = 0
        
        # Test sur 100 éléments
        biens = lire_csv_biens(chemin_csv, n_max=100)
        if nom == "Fusion":
            _, _, temps_100 = algo(biens, "prix")
        else:
            _, _, _, temps_100 = algo(biens, "prix")
        
        # Test sur 500 éléments
        biens = lire_csv_biens(chemin_csv, n_max=500)
        if nom == "Fusion":
            _, _, temps_500 = algo(biens, "prix")
        else:
            _, _, _, temps_500 = algo(biens, "prix")
        
        # Test sur 1000 éléments
        biens = lire_csv_biens(chemin_csv, n_max=1000)
        if nom == "Fusion":
            _, _, temps_1000 = algo(biens, "prix")
        else:
            _, _, _, temps_1000 = algo(biens, "prix")
        
        facteur_500 = temps_500 / temps_100 if temps_100 > 0 else 0
        facteur_1000 = temps_1000 / temps_100 if temps_100 > 0 else 0
        
        print(f"{nom:<15} : {facteur_500:>6.1f}x → {facteur_1000:>6.1f}x")

def generer_rapport_visualisation():
    """Génère un rapport de visualisation complet"""
    print("\n🎨 RAPPORT DE VISUALISATION COMPLET")
    print("=" * 60)
    
    # Générer les données
    temps_data, comp_data = generer_tableau_comparatif()
    
    # Graphiques
    tailles = [100, 500, 1000]
    generer_graphique_temps(tailles, temps_data)
    generer_graphique_comparaisons(tailles, comp_data)
    
    # Analyse de scalabilité
    generer_analyse_scalabilite()
    
    print("\n🏆 CONCLUSIONS VISUELLES :")
    print("  • 🥇 Tri Fusion : Le plus rapide et stable")
    print("  • 🥈 Tri Rapide : Très rapide mais moins stable")
    print("  • 🥉 Tri par Tas : Performance garantie")
    print("  • 🐌 Tri Sélection : Le plus lent (O(n²))")
    print("  • 📊 Tri Insertion : Moyen, efficace sur petites données")

def main():
    """Fonction principale de visualisation"""
    print("🎨 VISUALISATION DES PERFORMANCES")
    print("=" * 40)
    
    while True:
        print("\nOptions de visualisation :")
        print("1. 📊 Graphique des temps d'exécution")
        print("2. 🔍 Graphique des comparaisons")
        print("3. 📋 Tableau comparatif complet")
        print("4. 📈 Analyse de scalabilité")
        print("5. 🎨 Rapport de visualisation complet")
        print("0. ❌ Retour")
        
        choix = input("\nVotre choix (0-5) : ").strip()
        
        if choix == "1":
            temps_data, _ = generer_tableau_comparatif()
            generer_graphique_temps([100, 500, 1000], temps_data)
        elif choix == "2":
            _, comp_data = generer_tableau_comparatif()
            generer_graphique_comparaisons([100, 500, 1000], comp_data)
        elif choix == "3":
            generer_tableau_comparatif()
        elif choix == "4":
            generer_analyse_scalabilite()
        elif choix == "5":
            generer_rapport_visualisation()
        elif choix == "0":
            break
        else:
            print("❌ Choix invalide")
        
        input("\nAppuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main() 