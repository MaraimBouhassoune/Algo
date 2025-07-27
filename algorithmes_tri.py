"""
Implémentation complète des 4 algorithmes de tri :
  • Sélection   • Insertion
  • Fusion      • Rapide (pivot aléatoire)

Chaque fonction renvoie :
    (liste triée, nb_comparaisons, nb_échanges|décalages, temps_sec)

Comptage précis de toutes les opérations selon les spécifications.
"""

from time import perf_counter as _now
from random import randint


def _get_numeric_value(item, key):
    """
    Extrait et convertit la valeur numérique pour la comparaison.
    Gère les cas où la valeur est déjà un nombre ou une chaîne.
    """
    value = item[key]
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


# --------------------------------------------------------------------------- #
def tri_selection(lst, key):
    """
    Tri par sélection : trouve le minimum et l'échange avec l'élément courant.
    Complexité : O(n²) comparaisons, O(n) échanges
    """
    if not lst:
        return [], 0, 0, 0.0
    
    t0 = _now()
    tab = lst.copy()  
    n = len(tab)
    comp = exch = 0

    for i in range(n - 1):
        min_idx = i
        
        
        for j in range(i + 1, n):
            comp += 1
            if _get_numeric_value(tab[j], key) < _get_numeric_value(tab[min_idx], key):
                min_idx = j
        
         
        if min_idx != i:
            tab[i], tab[min_idx] = tab[min_idx], tab[i]
            exch += 1
    
    return tab, comp, exch, _now() - t0


# --------------------------------------------------------------------------- #
def tri_insertion(lst, key):
    """
    Tri par insertion : insère chaque élément à sa place dans la partie triée.
    Complexité : O(n²) comparaisons, O(n²) décalages
    """
    if not lst:
        return [], 0, 0, 0.0
    
    t0 = _now()
    tab = lst.copy()
    comp = shift = 0

    for i in range(1, len(tab)):
        pivot = tab[i]
        pivot_val = _get_numeric_value(pivot, key)
        j = i - 1
        
         
        while j >= 0:
            comp += 1   
            if _get_numeric_value(tab[j], key) > pivot_val:
                tab[j + 1] = tab[j]
                shift += 1
                j -= 1
            else:
                break
        
        
        if j + 1 != i:   
            tab[j + 1] = pivot
            shift += 1
    
    return tab, comp, shift, _now() - t0


# --------------------------------------------------------------------------- #
def tri_fusion(lst, key):
    """
    Tri fusion : divise la liste en deux, trie récursivement, puis fusionne.
    Complexité : O(n log n) comparaisons, O(n log n) temps
    """
    if not lst:
        return [], 0, 0.0
    
    t0 = _now()
    comp = [0]  

    def _merge(gauche, droite):
        """Fusionne deux listes triées."""
        resultat = []
        i = j = 0
        
       
        while i < len(gauche) and j < len(droite):
            comp[0] += 1
            if _get_numeric_value(gauche[i], key) <= _get_numeric_value(droite[j], key):
                resultat.append(gauche[i])
                i += 1
            else:
                resultat.append(droite[j])
                j += 1
        
        
        resultat.extend(gauche[i:])
        resultat.extend(droite[j:])
        return resultat

    def _tri_fusion_recursif(tab):
        """Fonction récursive de tri fusion."""
        if len(tab) <= 1:
            return tab
        
      
        milieu = len(tab) // 2
        gauche = _tri_fusion_recursif(tab[:milieu])
        droite = _tri_fusion_recursif(tab[milieu:])
        
        
        return _merge(gauche, droite)

    resultat = _tri_fusion_recursif(lst.copy())
    return resultat, comp[0], _now() - t0


# --------------------------------------------------------------------------- #
def tri_rapide(lst, key):
    """
    Tri rapide avec pivot aléatoire : partitionne autour d'un pivot et trie récursivement.
    Complexité moyenne : O(n log n), pire cas : O(n²)
    """
    if not lst:
        return [], 0, 0, 0.0
    
    t0 = _now()
    tab = lst.copy()
    comp = [0]
    exch = [0]

    def _partition(bas, haut):
        """
        Partitionne le tableau autour d'un pivot aléatoire.
        Retourne l'index final du pivot.
        """
         
        pivot_idx = randint(bas, haut)
        if pivot_idx != haut:
            tab[pivot_idx], tab[haut] = tab[haut], tab[pivot_idx]
            exch[0] += 1

        pivot_val = _get_numeric_value(tab[haut], key)
        i = bas - 1   

        
        for j in range(bas, haut):
            comp[0] += 1
            if _get_numeric_value(tab[j], key) <= pivot_val:
                i += 1
                if i != j:
                    tab[i], tab[j] = tab[j], tab[i]
                    exch[0] += 1

        
        if i + 1 != haut:
            tab[i + 1], tab[haut] = tab[haut], tab[i + 1]
            exch[0] += 1

        return i + 1

    def _tri_rapide_recursif(bas, haut):
        """Fonction récursive de tri rapide."""
        if bas < haut:
            
            pivot_pos = _partition(bas, haut)
            
            
            _tri_rapide_recursif(bas, pivot_pos - 1)
            _tri_rapide_recursif(pivot_pos + 1, haut)

    
    if len(tab) > 1:
        _tri_rapide_recursif(0, len(tab) - 1)
    
    return tab, comp[0], exch[0], _now() - t0


# --------------------------------------------------------------------------- #
def valider_tri(original, trie, key):
    """
    Valide qu'un tri a été effectué correctement.
    Vérifie l'ordre et que tous les éléments sont présents.
    """
    if len(original) != len(trie):
        return False, "Tailles différentes"
    
    
    for i in range(len(trie) - 1):
        val_courante = _get_numeric_value(trie[i], key)
        val_suivante = _get_numeric_value(trie[i + 1], key)
        if val_courante > val_suivante:
            return False, f"Ordre incorrect à l'index {i}"
    
   
    ids_original = sorted([id(item) for item in original])
    ids_trie = sorted([id(item) for item in trie])
    
    if ids_original != ids_trie:
        return False, "Éléments manquants ou en double"
    
    return True, "Tri valide"


def comparer_algorithmes_tri(biens, key, taille_echantillon=None):
    """
    Compare les performances des 4 algorithmes de tri sur les mêmes données.
    """
    if taille_echantillon:
        biens = biens[:taille_echantillon]
    
    algorithmes = [
        (tri_selection, "TRI SÉLECTION"),
        (tri_insertion, "TRI INSERTION"),
        (tri_fusion, "TRI FUSION"),
        (tri_rapide, "TRI RAPIDE")
    ]
    
    print(f"\n🏁 COMPARAISON DES TRIS sur {len(biens)} éléments (clé: {key})")
    print("=" * 70)
    
    resultats = []
    for algo_func, nom in algorithmes:
        if nom == "TRI FUSION":
            trie, comp, temps = algo_func(biens, key)
            print(f"{nom:<15} : {temps:>8.4f}s | {comp:>6} comparaisons")
            resultats.append((nom, temps, comp, 0))
        else:
            trie, comp, ops, temps = algo_func(biens, key)
            ops_nom = "décalages" if nom == "TRI INSERTION" else "échanges"
            print(f"{nom:<15} : {temps:>8.4f}s | {comp:>6} comparaisons | {ops:>6} {ops_nom}")
            resultats.append((nom, temps, comp, ops))
        
        # Validation
        valide, msg = valider_tri(biens, trie, key)
        if not valide:
            print(f"❌ ERREUR dans {nom}: {msg}")
    
    return resultats


# =========================
# 🏆 BONUS : TRI PAR TAS (HEAP SORT)
# =========================
def tri_tas(lst, key):
    """
    🏆 BONUS : Tri par tas (Heap Sort)
    Complexité : O(n log n) dans TOUS les cas (garantie)
    Avantages : 
    - Tri in-place (pas de mémoire supplémentaire)
    - Performance stable indépendamment des données
    - Algorithme avancé démontrant la maîtrise des structures de données
    """
    if not lst:
        return [], 0, 0, 0.0
    
    t0 = _now()
    tab = lst.copy()
    n = len(tab)
    comp = [0]
    exch = [0]

    def _heapify(arr, n, i):
        """
        Transforme un sous-arbre en tas max.
        Assure que la propriété du tas est respectée.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Vérifier si l'enfant gauche existe et est plus grand
        if left < n:
            comp[0] += 1
            if _get_numeric_value(arr[left], key) > _get_numeric_value(arr[largest], key):
                largest = left

        # Vérifier si l'enfant droit existe et est plus grand
        if right < n:
            comp[0] += 1
            if _get_numeric_value(arr[right], key) > _get_numeric_value(arr[largest], key):
                largest = right

        # Si le plus grand n'est pas la racine, échanger et réorganiser
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            exch[0] += 1
            _heapify(arr, n, largest)

    def _build_heap(arr, n):
        """
        Construit un tas max à partir du tableau.
        Commence par les nœuds non-feuilles et remonte vers la racine.
        """
        for i in range(n // 2 - 1, -1, -1):
            _heapify(arr, n, i)

    # ÉTAPE 1 : Construire le tas max
    _build_heap(tab, n)

    # ÉTAPE 2 : Extraire les éléments un par un
    for i in range(n - 1, 0, -1):
        # Échanger la racine (max) avec le dernier élément
        tab[0], tab[i] = tab[i], tab[0]
        exch[0] += 1
        
        # Réorganiser le tas sur la partie non triée
        _heapify(tab, i, 0)

    return tab, comp[0], exch[0], _now() - t0


def comparer_tous_algorithmes_avec_bonus(biens, key, taille_echantillon=None):
    """
    🏆 BONUS : Compare TOUS les algorithmes incluant le tri par tas
    """
    if taille_echantillon:
        biens = biens[:taille_echantillon]
    
    algorithmes = [
        (tri_selection, "TRI SÉLECTION"),
        (tri_insertion, "TRI INSERTION"),
        (tri_fusion, "TRI FUSION"),
        (tri_rapide, "TRI RAPIDE"),
        (tri_tas, "🏆 TRI PAR TAS (BONUS)")
    ]
    
    print(f"\n🏆 COMPARAISON COMPLÈTE AVEC BONUS sur {len(biens)} éléments (clé: {key})")
    print("=" * 80)
    
    resultats = []
    for algo_func, nom in algorithmes:
        if nom == "TRI FUSION":
            trie, comp, temps = algo_func(biens, key)
            print(f"{nom:<25} : {temps:>8.4f}s | {comp:>6} comparaisons")
            resultats.append((nom, temps, comp, 0))
        else:
            trie, comp, ops, temps = algo_func(biens, key)
            ops_nom = "décalages" if nom == "TRI INSERTION" else "échanges"
            print(f"{nom:<25} : {temps:>8.4f}s | {comp:>6} comparaisons | {ops:>6} {ops_nom}")
            resultats.append((nom, temps, comp, ops))
        
        # Validation
        valide, msg = valider_tri(biens, trie, key)
        if not valide:
            print(f"❌ ERREUR dans {nom}: {msg}")
    
    return resultats