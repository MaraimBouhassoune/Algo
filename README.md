# PROJET ALGORITHMIE - ANALYSE DE PERFORMANCE

## 📋 Description

Ce projet implémente **from scratch** et compare les performances de 7 algorithmes fondamentaux sur des données réelles d'immobilier :

### 🔄 Algorithmes de tri (4)
- **Tri par sélection** : O(n²) - Simple et prévisible
- **Tri par insertion** : O(n²) - Efficace sur petites données
- **Tri fusion** : O(n log n) - Stable et optimal
- **Tri rapide** : O(n log n) moyenne - Rapide en pratique

### 🔍 Algorithmes de recherche (3)  
- **Recherche linéaire** : O(n) - Universelle
- **Recherche binaire** : O(log n) - Sur données triées
- **Recherche Min/Max** : O(n) - Optimisée en un parcours

## 🎯 Objectifs pédagogiques

1. **Implémenter** les algorithmes sans bibliothèques externes
2. **Mesurer** précisément temps d'exécution et nombre d'opérations
3. **Comparer** théorie vs pratique sur données réelles
4. **Analyser** les résultats et formuler des recommandations

## 📁 Structure du projet

```
projet-algorithmie/
│
├── 📄 transactions_immobilieres.csv  # Dataset (fourni)
├── 🐍 utilitaires.py                 # Lecture CSV from scratch
├── 🔄 algorithmes_tri.py             # 4 algorithmes de tri
├── 🔍 algorithmes_recherche.py       # 3 algorithmes de recherche
├── 🚀 main.py                        # Exécution des tests
├── 🧪 test_validation.py             # Tests de validation
├── 📊 resultats.txt                  # Résultats bruts (généré)
├── 📈 analyse_complete.txt           # Rapport d'analyse (généré)
└── 📖 README.md                      # Ce fichier
```

## 🚀 Utilisation

### Prérequis
- Python 3.6+ (aucune bibliothèque externe)
- Fichier `transactions_immobilieres.csv` dans le même dossier

### Exécution principale
```bash
python main.py
```

Cette commande :
1. ✅ Charge et valide les données CSV
2. 🔄 Teste les 4 tris sur 2 critères × 3 tailles (24 tests)
3. 🔍 Teste les 3 recherches sur 3 tailles (12 tests) 
4. 📊 Génère `resultats.txt` et `analyse_complete.txt`

### Tests de validation
```bash
python test_validation.py
```

Valide automatiquement :
- ✅ Implémentation correcte des algorithmes
- ✅ Comptage précis des opérations
- ✅ Conformité au cahier des charges

### Tests sur données fictives
```bash
python test_recherche.py
```

Teste rapidement sur un petit échantillon de 10 biens.

## 📊 Types de tests effectués

### Tests de tri
- **Tailles** : 100, 500, 1000 éléments
- **Critères** : Prix et Surface
- **Mesures** : Temps, comparaisons, échanges/décalages

### Tests de recherche
- **Recherche linéaire** : Maisons à Paris, Appartements 3 pièces
- **Recherche binaire** : Prix exact (350000€)
- **Min/Max** : Prix au m² minimum et maximum

## 📈 Résultats générés

### `resultats.txt`
Format brut compatible avec les spécifications :
```
=== TRI PAR PRIX (1000 éléments) ===  
Tri SÉLECTION : 0.165648s | 498501 comparaisons | 993 échanges
Tri INSERTION : 0.105827s | 252923 comparaisons | 252915 décalages
Tri FUSION : 0.004948s | 8696 comparaisons
Tri RAPIDE : 0.005510s | 12806 comparaisons | 4921 échanges
```

### `analyse_complete.txt`
Rapport détaillé avec :
- 📊 Classements par performance
- 🔍 Analyses comparatives 
- 💡 Recommandations d'usage
- 📈 Observations théorie vs pratique

## 🛠️ Implémentation technique

### Lecture CSV robuste
```python
def lire_csv_biens(path, n_max=None):
    # Gestion des virgules dans les données
    # Conversion automatique des types
    # Validation de l'intégrité
```

### Comptage précis des opérations
- **Comparaisons** : Chaque test de condition
- **Échanges** : Chaque permutation d'éléments
- **Décalages** : Chaque déplacement en insertion

### Mesure temporelle haute précision
```python
from time import perf_counter
t0 = perf_counter()
# ... algorithme ...
temps = perf_counter() - t0
```

## 🎯 Conformité cahier des charges

✅ **4 algorithmes de tri** implémentés from scratch  
✅ **3 algorithmes de recherche** implémentés from scratch  
✅ **Tests sur 3 tailles** : 100, 500, 1000 éléments  
✅ **Mesure temps + opérations** pour chaque algorithme  
✅ **Lecture CSV** sans bibliothèque externe  
✅ **Analyse comparative** des résultats  
✅ **Rapport détaillé** des observations  

## 🔧 Personnalisation

### Modifier les tailles de test
```python
# Dans main.py
TAILLES_TEST = [50, 200, 1500]  # Nouvelles tailles
```

### Ajouter des critères de tri
```python  
# Dans main.py
CRITERES_TRI = [
    ("prix", "PRIX"),
    ("surface", "SURFACE"), 
    ("prix_m2", "PRIX_M2")  # Nouveau critère
]
```

### Tests sur d'autres recherches
```python
# Dans algorithmes_recherche.py
nb, comp, temps = recherche_lineaire(
    biens,
    lambda x: x["commune"] == "MARSEILLE"  # Nouvelle condition
)
```

