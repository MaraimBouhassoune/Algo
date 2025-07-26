# Projet : Analyse de performance d'algorithmes (Tri et Recherche)

## Objectif
Ce projet a pour but de comparer les performances de plusieurs algorithmes de tri et de recherche sur des données réelles d'immobilier. On mesure le temps d'exécution, le nombre de comparaisons et d'opérations pour chaque algorithme, puis on analyse les résultats.

## Structure du projet

```
├── main.py                  # Programme principal qui lance tous les tests
├── algorithmes_tri.py       # Les 4 algorithmes de tri (sélection, insertion, fusion, rapide)
├── algorithmes_recherche.py # Les 3 algorithmes de recherche 
├── utilitaires.py           # Fonctions pour lire le CSV et autres utilitaires
├── transactions_immobilieres.csv # Données fournies (ne pas modifier)
├── resultats.txt            # Résultats des tests (généré automatiquement)
├── analyse.txt              # Réponses aux questions d'analyse
```

## Comment exécuter le projet
1. Placez le fichier `transactions_immobilieres.csv` dans le dossier du projet.
2. Lancez le programme principal :
   ```bash
   python main.py
   ```
3. Les résultats des tris s'affichent à l'écran et sont enregistrés dans `resultats.txt`.
4. Lisez `analyse.txt` pour voir les réponses aux questions d'analyse.

## Ce que fait chaque fichier
- **main.py** : lance les tests de tri et de recherche, affiche et sauvegarde les résultats.
- **algorithmes_tri.py** : contient les fonctions de tri, chacune compte les comparaisons, échanges/décalages, temps.
- **algorithmes_recherche.py** : contiendra les fonctions de recherche (linéaire, binaire, min/max).
- **utilitaires.py** : lit le CSV sans bibliothèque externe, retourne les données sous forme de liste de dictionnaires.
- **resultats.txt** : tous les résultats des tests, au format demandé.
- **analyse.txt** : réponses aux questions d'analyse.

---
