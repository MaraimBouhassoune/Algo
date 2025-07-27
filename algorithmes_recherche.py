"""
3 algorithmes de recherche avec comptage précis des opérations :
  • Linéaire (compte ou position)
  • Binaire (nécessite tableau trié)
  • Min/Max (un seul parcours)

Chaque fonction renvoie les résultats + nombre de comparaisons + temps
"""

from time import perf_counter as _now


def _get_numeric_value(item, key):
    """
    Extrait et convertit la valeur numérique pour la comparaison.
    """
    value = item[key]
    if isinstance(value, (int, float)):
        return float(value)
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


# --------------------------------------------------------------------------- #
def recherche_lineaire(table, predicate):
    """
    Recherche linéaire avec prédicat personnalisé.
    Compte tous les éléments qui satisfont la condition.
    
    Args:
        table: Liste d'éléments à parcourir
        predicate: Fonction qui retourne True/False pour chaque élément
    
    Returns:
        (nombre_trouvés, comparaisons, temps)
    """
    if not table:
        return 0, 0, 0.0
    
    found = comp = 0
    t0 = _now()
    
    for elt in table:
        comp += 1  
        if predicate(elt):
            found += 1
    
    return found, comp, _now() - t0


def recherche_lineaire_position(table, cible, key):
    """
    Recherche linéaire pour trouver la PREMIÈRE position d'une valeur.
    S'arrête dès qu'elle trouve la valeur.
    
    Args:
        table: Liste d'éléments à parcourir
        cible: Valeur recherchée
        key: Clé du dictionnaire à comparer
    
    Returns:
        (position | -1, comparaisons, temps)
    """
    if not table:
        return -1, 0, 0.0
    
    comp = 0
    t0 = _now()
    
    for i, elt in enumerate(table):
        comp += 1
        if _get_numeric_value(elt, key) == cible:
            return i, comp, _now() - t0
    
    return -1, comp, _now() - t0


# --------------------------------------------------------------------------- #
def recherche_binaire(sorted_table, cible, key):
    """
    Recherche binaire dans un tableau TRIÉ.
    Divise l'espace de recherche en deux à chaque étape.
    
    Args:
        sorted_table: Liste triée par la clé spécifiée
        cible: Valeur numérique recherchée
        key: Clé du dictionnaire à comparer
    
    Returns:
        (position | -1, comparaisons, temps)
    """
    if not sorted_table:
        return -1, 0, 0.0
    
    gauche, droite = 0, len(sorted_table) - 1
    comp = 0
    t0 = _now()
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        val_milieu = _get_numeric_value(sorted_table[milieu], key)
        
        comp += 1   
        
        if val_milieu == cible:
            return milieu, comp, _now() - t0
        elif val_milieu < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    return -1, comp, _now() - t0


# --------------------------------------------------------------------------- #
def recherche_min_max(table, key):
    """
    Trouve le minimum et maximum en un seul parcours.
    Optimisé pour faire exactement 2*(n-1) comparaisons.
    
    Args:
        table: Liste d'éléments
        key: Clé du dictionnaire à analyser
    
    Returns:
        (min_val, max_val, comparaisons, temps)
    """
    if not table:
        return None, None, 0, 0.0
    
    if len(table) == 1:
        val = _get_numeric_value(table[0], key)
        return val, val, 0, 0.0
    
    t0 = _now()
    
    
    val_init = _get_numeric_value(table[0], key)
    val_min = val_max = val_init
    comp = 0
    
   
    for elt in table[1:]:
        val_courante = _get_numeric_value(elt, key)
        
       
        comp += 1
        if val_courante < val_min:
            val_min = val_courante
        
      
        comp += 1
        if val_courante > val_max:
            val_max = val_courante
    
    return val_min, val_max, comp, _now() - t0


# --------------------------------------------------------------------------- #
def recherche_lineaire_multiple(table, key, valeur):
    """
    Trouve TOUTES les positions d'une valeur dans le tableau.
    Utile quand il peut y avoir des doublons.
    
    Args:
        table: Liste d'éléments
        key: Clé du dictionnaire à comparer
        valeur: Valeur recherchée
    
    Returns:
        (liste_positions, comparaisons, temps)
    """
    if not table:
        return [], 0, 0.0
    
    positions = []
    comp = 0
    t0 = _now()
    
    for i, elt in enumerate(table):
        comp += 1
        if _get_numeric_value(elt, key) == valeur:
            positions.append(i)
    
    return positions, comp, _now() - t0


def recherche_dans_plage(table, key, min_val, max_val):
    """
    Trouve tous les éléments dans une plage de valeurs [min_val, max_val].
    
    Args:
        table: Liste d'éléments
        key: Clé du dictionnaire à comparer
        min_val: Valeur minimale (incluse)
        max_val: Valeur maximale (incluse)
    
    Returns:
        (elements_trouves, comparaisons, temps)
    """
    if not table:
        return [], 0, 0.0
    
    resultats = []
    comp = 0
    t0 = _now()
    
    for elt in table:
        val = _get_numeric_value(elt, key)
        comp += 2   
        if min_val <= val <= max_val:
            resultats.append(elt)
    
    return resultats, comp, _now() - t0


# --------------------------------------------------------------------------- #
def comparer_recherches(biens, biens_tries_prix):
    """
    Compare les performances des différents algorithmes de recherche.
    """
    print(f"\n🔍 COMPARAISON DES RECHERCHES sur {len(biens)} éléments")
    print("=" * 70)
    
     
    nb, comp, temps = recherche_lineaire(
        biens, 
        lambda x: x.get("type_local") == "Maison" and x.get("commune") == "PARIS"
    )
    print(f"Recherche linéaire (maisons Paris)  : {temps:.6f}s | {comp:>4} comp | {nb:>2} trouvées")
    
    
    pos, comp, temps = recherche_binaire(biens_tries_prix, 350000, "prix")
    print(f"Recherche binaire (350000€)         : {temps:.6f}s | {comp:>4} comp | pos {pos}")
    
     
    min_val, max_val, comp, temps = recherche_min_max(biens, "prix_m2")
    print(f"Min/Max prix/m²                     : {temps:.6f}s | {comp:>4} comp | {min_val:.0f}-{max_val:.0f}€/m²")
    
  
    nb, comp, temps = recherche_lineaire(
        biens,
        lambda x: x.get("type_local") == "Appartement" and str(x.get("nb_pieces")) == "3"
    )
    print(f"Recherche linéaire (appart 3P)      : {temps:.6f}s | {comp:>4} comp | {nb:>2} trouvés")
    
    return True


def valider_recherche_binaire(table_triee, key):
    """
    Valide qu'une table est bien triée pour permettre la recherche binaire.
    """
    if len(table_triee) <= 1:
        return True, "Table trop petite pour être mal triée"
    
    for i in range(len(table_triee) - 1):
        val_courante = _get_numeric_value(table_triee[i], key)
        val_suivante = _get_numeric_value(table_triee[i + 1], key)
        if val_courante > val_suivante:
            return False, f"Table mal triée à l'index {i}: {val_courante} > {val_suivante}"
    
    return True, "Table correctement triée"


def analyser_repartition(biens, key):
    """
    Analyse la répartition des valeurs pour une clé donnée.
    Utile pour comprendre les performances des algorithmes.
    """
    if not biens:
        return
    
    valeurs = []
    for bien in biens:
        val = _get_numeric_value(bien, key)
        if val > 0:   
            valeurs.append(val)
    
    if not valeurs:
        print(f"Aucune valeur valide pour la clé '{key}'")
        return
    
    valeurs.sort()
    n = len(valeurs)
    
    print(f"\n📈 ANALYSE DE RÉPARTITION - {key}")
    print(f"   • Nombre de valeurs : {n}")
    print(f"   • Minimum : {valeurs[0]:,.0f}")
    print(f"   • Maximum : {valeurs[-1]:,.0f}")
    print(f"   • Médiane : {valeurs[n//2]:,.0f}")
    print(f"   • Étendue : {valeurs[-1] - valeurs[0]:,.0f}")
    
     
    q1 = valeurs[n//4]
    q3 = valeurs[3*n//4]
    print(f"   • Q1 : {q1:,.0f}")
    print(f"   • Q3 : {q3:,.0f}")
    
    
    valeurs_uniques = len(set(valeurs))
    print(f"   • Valeurs uniques : {valeurs_uniques} ({100*valeurs_uniques/n:.1f}%)")