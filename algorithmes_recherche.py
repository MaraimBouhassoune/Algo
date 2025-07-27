"""
algorithmes_recherche.py
Squelettes des 3 algorithmes de recherche pour le projet d'analyse de performance.
Chaque fonction retourne les résultats et les compteurs demandés.
"""

import time

def convertir_valeur(valeur, cle):
    """
    Convertit une valeur en nombre selon la clé.
    Gère les cas où la valeur est une chaîne de caractères.
    """
    if isinstance(valeur, (int, float)):
        return valeur
    try:
        if cle in ['prix', 'surface', 'nb_pieces']:
            return int(valeur)
        elif cle in ['prix_m2']:
            return float(valeur)
        else:
            return valeur
    except (ValueError, TypeError):
        return valeur


def recherche_lineaire(tableau, critere_fonction):
    """
    Recherche linéaire : compte le nombre d'éléments vérifiant un critère.
    Args:
        tableau (list): Liste de dictionnaires ou tuples représentant les biens.
        critere_fonction (callable): Fonction prenant un élément et retournant True/False.
    Returns:
        (nb_trouves, nb_comparaisons, temps_execution)
    """
    nb_trouves = 0
    nb_comparaisons = 0
    debut = time.time()
    for element in tableau:
        nb_comparaisons += 1
        if critere_fonction(element):
            nb_trouves += 1
    fin = time.time()
    temps_execution = fin - debut
    return nb_trouves, nb_comparaisons, temps_execution

def recherche_lineaire_position(tableau, valeur_cible, cle):
    """
    Recherche linéaire : trouve la position du premier élément égal à la valeur cible.
    Args:
        tableau (list): Liste de dictionnaires ou tuples.
        valeur_cible: Valeur à rechercher.
        cle (str): Clé pour accéder à la valeur.
    Returns:
        (position_trouvee, nb_comparaisons, temps_execution)
        position_trouvee = -1 si non trouvé
    """
    debut = time.time()
    nb_comparaisons = 0
    position_trouvee = -1
    
    for i, element in enumerate(tableau):
        nb_comparaisons += 1
        valeur = convertir_valeur(element[cle], cle)
        if valeur == valeur_cible:
            position_trouvee = i
            break
    
    fin = time.time()
    temps_execution = fin - debut
    return position_trouvee, nb_comparaisons, temps_execution


def recherche_binaire(tableau, valeur_cible, cle):
    """
    Recherche binaire sur un tableau trié selon la clé donnée.
    Args:
        tableau (list): Liste triée de dictionnaires ou tuples.
        valeur_cible (int/float): Valeur à rechercher.
        cle (str): Clé ou index pour accéder à la valeur à comparer.
    Returns:
        (position_trouvee, nb_comparaisons, temps_execution)
        position_trouvee = -1 si non trouvé
    """
    debut = time.time()
    gauche = 0
    droite = len(tableau) - 1
    nb_comparaisons = 0
    position_trouvee = -1
    
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        valeur_str = tableau[milieu][cle]
        valeur = convertir_valeur(valeur_str, cle)
        nb_comparaisons += 1
        
        if valeur == valeur_cible:
            position_trouvee = milieu
            break
        elif valeur < valeur_cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    
    fin = time.time()
    temps_execution = fin - debut
    return position_trouvee, nb_comparaisons, temps_execution

def recherche_min_max(tableau, cle):
    """
    Recherche la valeur minimale ET maximale d'une colonne en un seul parcours.
    Args:
        tableau (list): Liste de dictionnaires ou tuples.
        cle (str): Clé ou index pour accéder à la valeur.
    Returns:
        (valeur_min, valeur_max, nb_comparaisons, temps_execution)
    """
    if not tableau:
        return None, None, 0, 0.0
    
    debut = time.time()
    valeur_min_str = tableau[0][cle]
    valeur_max_str = tableau[0][cle]
    valeur_min = convertir_valeur(valeur_min_str, cle)
    valeur_max = convertir_valeur(valeur_max_str, cle)
    nb_comparaisons = 0
    
    for element in tableau[1:]:
        val_str = element[cle]
        val = convertir_valeur(val_str, cle)
        nb_comparaisons += 1
        if val < valeur_min:
            valeur_min = val
        nb_comparaisons += 1
        if val > valeur_max:
            valeur_max = val
    
    fin = time.time()
    temps_execution = fin - debut
    return valeur_min, valeur_max, nb_comparaisons, temps_execution


def format_resultat_recherche_lineaire(temps, nb_comp, nb_trouves):
    return f"Recherche linéaire : {temps:.4f}s | {nb_comp} comparaisons | Trouvées: {nb_trouves}"

def format_resultat_recherche_binaire(temps, nb_comp, pos):
    return f"Recherche binaire : {temps:.4f}s | {nb_comp} comparaisons | Position: {pos}"

def format_resultat_min_max(temps, nb_comp, vmin, vmax):
    return f"Min/Max : {temps:.4f}s | {nb_comp} comparaisons | Min: {vmin} | Max: {vmax}"

