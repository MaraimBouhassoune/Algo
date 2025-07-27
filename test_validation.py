"""
Tests de validation pour vérifier que le projet respecte le cahier des charges.
Ce fichier permet de valider automatiquement l'implémentation.
"""

def test_imports():
    """Test que tous les modules se chargent correctement."""
    print("🧪 TEST : Imports des modules")
    
    try:
        from utilitaires import lire_csv_biens, convert_value, parse_csv_line
        print("   ✅ utilitaires.py importé")
    except ImportError as e:
        print(f"   ❌ Erreur import utilitaires: {e}")
        return False
    
    try:
        from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide, valider_tri
        print("   ✅ algorithmes_tri.py importé")
    except ImportError as e:
        print(f"   ❌ Erreur import algorithmes_tri: {e}")
        return False
    
    try:
        from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max
        print("   ✅ algorithmes_recherche.py importé")
    except ImportError as e:
        print(f"   ❌ Erreur import algorithmes_recherche: {e}")
        return False
    
    return True


def test_lecture_csv():
    """Test de la fonction de lecture CSV."""
    print("\n🧪 TEST : Lecture du fichier CSV")
    
    try:
        from utilitaires import lire_csv_biens, convert_value, parse_csv_line
        
      
        assert convert_value("250000", "prix") == 250000
        assert convert_value("3846.5", "prix_m2") == 3846.5
        assert convert_value("PARIS", "commune") == "PARIS"
        print("   ✅ Conversion des valeurs : OK")
        
      
        ligne_test = '2023-01-15,250000,65,PARIS,Appartement,2,75001,3846'
        valeurs = parse_csv_line(ligne_test)
        assert len(valeurs) == 8
        assert valeurs[1] == '250000'
        assert valeurs[3] == 'PARIS'
        print("   ✅ Parsing CSV : OK")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erreur test CSV: {e}")
        return False


def test_algorithmes_tri():
    """Test des 4 algorithmes de tri."""
    print("\n🧪 TEST : Algorithmes de tri")
    
    try:
        from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide, valider_tri
        
    
        biens_test = [
            {"prix": 300, "surface": 80, "nom": "Bien1"},
            {"prix": 150, "surface": 50, "nom": "Bien2"},
            {"prix": 450, "surface": 120, "nom": "Bien3"},
            {"prix": 200, "surface": 60, "nom": "Bien4"},
        ]
        
        prix_attendus = [150, 200, 300, 450]
        
        algorithmes = [
            (tri_selection, "Sélection"),
            (tri_insertion, "Insertion"),
            (tri_fusion, "Fusion"),
            (tri_rapide, "Rapide")
        ]
        
        for algo_func, nom in algorithmes:
            try:
                if nom == "Fusion":
                    trie, comp, temps = algo_func(biens_test, "prix")
                    assert temps >= 0, f"Temps négatif pour {nom}"
                    assert comp > 0, f"Aucune comparaison pour {nom}"
                else:
                    trie, comp, ops, temps = algo_func(biens_test, "prix")
                    assert temps >= 0, f"Temps négatif pour {nom}"
                    assert comp > 0, f"Aucune comparaison pour {nom}"
                    assert ops >= 0, f"Opérations négatives pour {nom}"
                
             
                prix_trie = [bien["prix"] for bien in trie]
                assert prix_trie == prix_attendus, f"Tri incorrect pour {nom}: {prix_trie}"
                
                print(f"   ✅ {nom} : OK ({comp} comparaisons)")
                
            except Exception as e:
                print(f"   ❌ Erreur {nom}: {e}")
                return False
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erreur générale tri: {e}")
        return False


def test_algorithmes_recherche():
    """Test des 3 algorithmes de recherche."""
    print("\n🧪 TEST : Algorithmes de recherche")
    
    try:
        from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max
        
    
        biens_test = [
            {"prix": 150, "surface": 50, "type_local": "Appartement", "commune": "PARIS", "nb_pieces": "2", "prix_m2": 3000},
            {"prix": 200, "surface": 60, "type_local": "Maison", "commune": "PARIS", "nb_pieces": "3", "prix_m2": 3333},
            {"prix": 300, "surface": 80, "type_local": "Appartement", "commune": "LYON", "nb_pieces": "3", "prix_m2": 3750},
            {"prix": 350, "surface": 90, "type_local": "Appartement", "commune": "PARIS", "nb_pieces": "3", "prix_m2": 3889},
        ]
        
     
        nb_paris, comp, temps = recherche_lineaire(
            biens_test, 
            lambda x: x["commune"] == "PARIS"
        )
        assert nb_paris == 3, f"Recherche linéaire incorrecte: {nb_paris} != 3"
        assert comp == 4, f"Nombre de comparaisons incorrect: {comp} != 4"
        print(f"   ✅ Recherche linéaire : OK ({nb_paris} trouvés, {comp} comparaisons)")
        
        
        biens_tries = sorted(biens_test, key=lambda x: x["prix"])
        pos, comp, temps = recherche_binaire(biens_tries, 300, "prix")
        assert pos >= 0, f"Position invalide: {pos}"
        print(f"   ✅ Recherche binaire : OK (position {pos}, {comp} comparaisons)")
        
        
        min_prix, max_prix, comp, temps = recherche_min_max(biens_test, "prix")
        assert min_prix == 150, f"Prix minimum incorrect: {min_prix} != 150"
        assert max_prix == 350, f"Prix maximum incorrect: {max_prix} != 350"
        print(f"   ✅ Min/Max : OK ({min_prix}-{max_prix}, {comp} comparaisons)")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erreur test recherche: {e}")
        return False


def test_fichier_csv():
    """Test de l'existence et lisibilité du fichier CSV."""
    print("\n🧪 TEST : Fichier CSV")
    
    try:
        import os
        from utilitaires import lire_csv_biens
        

        if not os.path.exists("transactions_immobilieres.csv"):
            print("   ❌ Fichier transactions_immobilieres.csv non trouvé")
            return False
        
      
        biens = lire_csv_biens("transactions_immobilieres.csv", n_max=10)
        if len(biens) == 0:
            print("   ❌ Aucune donnée lue du fichier CSV")
            return False
        
    
        premier_bien = biens[0]
        champs_requis = ['prix', 'surface', 'commune', 'type_local']
        for champ in champs_requis:
            if champ not in premier_bien:
                print(f"   ❌ Champ '{champ}' manquant")
                return False
        
        print(f"   ✅ Fichier CSV : OK ({len(biens)} biens lus)")
        return True
        
    except Exception as e:
        print(f"   ❌ Erreur fichier CSV: {e}")
        return False


def test_conformite_cahier_charges():
    """Test de conformité avec le cahier des charges."""
    print("\n🧪 TEST : Conformité cahier des charges")
    
    checks = []
   
    try:
        from algorithmes_tri import tri_selection, tri_insertion, tri_fusion, tri_rapide
        checks.append("✅ 4 algorithmes de tri implémentés")
    except ImportError as e:
        checks.append(f"❌ Algorithmes de tri manquants : {e}")
    
    
    try:
        from algorithmes_recherche import recherche_lineaire, recherche_binaire, recherche_min_max
        checks.append("✅ 3 algorithmes de recherche implémentés")
    except ImportError as e:
        checks.append(f"❌ Algorithmes de recherche manquants : {e}")
    
    
    import os
    if os.path.exists("main.py"):
        checks.append("✅ Fichier main.py présent")
    else:
        checks.append("❌ Fichier main.py manquant")
    
    
    try:
        from algorithmes_tri import tri_selection
        biens_test = [{"prix": 100}, {"prix": 200}]
        _, comp, _, _ = tri_selection(biens_test, "prix")
        assert comp > 0, "Pas de comptage des comparaisons"
        checks.append("✅ Comptage des opérations implémenté")
    except Exception as e:
        checks.append(f"❌ Problème comptage opérations : {e}")
    
 
    if os.path.exists("resultats.txt"):
        checks.append("✅ Fichier resultats.txt généré")
    else:
        checks.append("⚠️  Fichier resultats.txt non trouvé (exécuter main.py)")
    
   
    for check in checks:
        print(f"   {check}")
    
    
    score = sum(1 for check in checks if check.startswith("✅"))
    total = len(checks)
    print(f"\n   📊 SCORE DE CONFORMITÉ : {score}/{total} ({100*score/total:.0f}%)")
    
    return score >= total - 1  


def executer_tous_les_tests():
    """Exécute tous les tests de validation."""
    print("🧪 SUITE DE TESTS DE VALIDATION")
    print("=" * 50)
    
    tests = [
        ("Imports des modules", test_imports),
        ("Lecture CSV", test_lecture_csv),
        ("Algorithmes de tri", test_algorithmes_tri),
        ("Algorithmes de recherche", test_algorithmes_recherche),
        ("Fichier CSV", test_fichier_csv),
        ("Conformité cahier charges", test_conformite_cahier_charges),
    ]
    
    resultats = []
    
    for nom_test, fonction_test in tests:
        try:
            succes = fonction_test()
            if succes:
                resultats.append(True)
            else:
                resultats.append(False)
        except Exception as e:
            print(f"❌ ERREUR dans {nom_test}: {e}")
            resultats.append(False)
    
   
    print(f"\n🎯 RÉSUMÉ DES TESTS")
    print("=" * 20)
    reussis = sum(resultats)
    total = len(resultats)
    
    for i, (nom_test, _) in enumerate(tests):
        statut = "✅ RÉUSSI" if resultats[i] else "❌ ÉCHOUÉ"
        print(f"   {nom_test:<25} : {statut}")
    
    print(f"\n📊 SCORE GLOBAL : {reussis}/{total} ({100*reussis/total:.0f}%)")
    
    if reussis == total:
        print("🎉 TOUS LES TESTS SONT RÉUSSIS ! Le projet est conforme.")
    elif reussis >= total - 1:
        print("👍 PROJET GLOBALEMENT CONFORME (1 test mineur échoué)")
    else:
        print(f"⚠️  {total-reussis} test(s) à corriger.")
    
    return reussis >= total - 1


if __name__ == "__main__":
    try:
        executer_tous_les_tests()
    except Exception as e:
        print(f"❌ ERREUR CRITIQUE: {e}")
        print("Vérifiez que tous les fichiers sont présents dans le même dossier.")