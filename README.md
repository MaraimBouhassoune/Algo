# Projet : Analyse de Performance d'Algorithmes
## Tri et Recherche - Mesure et Comparaison

### 📋 Description du projet
Ce projet implémente et compare les performances de 7 algorithmes sur des données réelles d'immobilier :
- **4 algorithmes de tri** : sélection, insertion, fusion, rapide
- **3 algorithmes de recherche** : linéaire, binaire, min/max

### 🏗️ Structure du projet
```
Algo/
├── main.py                          # Programme principal (tris + recherches)
├── algorithmes_tri.py               # 4 algorithmes de tri
├── algorithmes_recherche.py         # 3 algorithmes de recherche
├── utilitaires.py                   # Lecture du CSV sans bibliothèque
├── test_recherche.py                # Tests isolés des recherches
├── transactions_immobilieres.csv    # Données d'immobilier
├── resultats.txt                    # Résultats des tests
├── analyse.txt                      # Analyse des résultats
└── README.md                        # Documentation
```

### 🚀 Comment lancer le projet

#### Option 1 : Tests complets (recommandé)
```bash
python main.py
```
Lance tous les tests :
- **Tris** : 4 algorithmes × 2 critères × 3 tailles = 24 tests
- **Recherches** : 4 types × 3 tailles = 12 tests

#### Option 2 : Tests de recherche uniquement
```bash
python test_recherche.py
```
Lance les tests de recherche sur un mini-tableau fictif (10 biens).

### 📊 Résultats obtenus

#### Algorithmes de Tri
- **Tri Fusion** : Le plus rapide (O(n log n))
- **Tri Rapide** : Très efficace mais moins stable
- **Tri Insertion** : Moyennement efficace (O(n²))
- **Tri Sélection** : Le plus lent (O(n²))

#### Algorithmes de Recherche
- **Recherche Binaire** : Très rapide (O(log n)) - 6-7 comparaisons sur 100-1000 éléments
- **Recherche Linéaire** : Linéaire (O(n)) - 100-999 comparaisons
- **Recherche Min/Max** : Efficace en un seul parcours

### 🔍 Tests de recherche effectués

#### Sur 100 éléments :
- Maisons à Paris : 5 trouvées
- Prix exact 350000€ : Position 50 (recherche binaire)
- Prix au m² : Min 1312€/m², Max 11702€/m²
- Appartements 3 pièces : 27 trouvés

#### Sur 500 éléments :
- Maisons à Paris : 10 trouvées
- Prix exact 350000€ : Position 295 (recherche binaire)
- Prix au m² : Min 985€/m², Max 12777€/m²
- Appartements 3 pièces : 60 trouvés

#### Sur 1000 éléments :
- Maisons à Paris : 17 trouvées
- Prix exact 350000€ : Position 600 (recherche binaire)
- Prix au m² : Min 985€/m², Max 13785€/m²
- Appartements 3 pièces : 91 trouvés

### 📈 Observations importantes

1. **Complexité algorithmique** : Les différences entre O(n²) et O(n log n) sont spectaculaires sur de gros volumes
2. **Recherche binaire** : 100x plus rapide que la recherche linéaire
3. **Stabilité** : Le tri fusion est plus stable que le tri rapide
4. **Données réelles** : Les performances varient selon la distribution des données
5. **Progression cohérente** : Les résultats évoluent logiquement avec la taille des données

### 🛠️ Technologies utilisées
- **Python** (sans bibliothèques externes)
- **Lecture CSV** manuelle (sans pandas/csv)
- **Mesure de temps** avec `time.time()`
- **Comptage manuel** des opérations

### 📝 Analyse complète
Consultez `analyse.txt` pour les réponses détaillées aux 10 questions d'analyse du projet.

### ✅ Validation
Le projet respecte toutes les contraintes :
- ✅ Implémentation FROM SCRATCH
- ✅ Pas de bibliothèques externes (csv, pandas, numpy)
- ✅ Comptage manuel des opérations
- ✅ Tests sur 3 tailles (100, 500, 1000)
- ✅ Format d'affichage respecté
- ✅ Sauvegarde dans resultats.txt
- ✅ Analyse complète dans analyse.txt
