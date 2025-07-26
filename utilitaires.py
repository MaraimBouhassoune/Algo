def lire_csv_biens(chemin_fichier, nb_elements=None):
    """
    Lit un fichier CSV d'immobilier et retourne une liste de dictionnaires.
    :param chemin_fichier: chemin du fichier CSV
    :param nb_elements: nombre d'éléments à lire (None = tout)
    :return: liste de dictionnaires
    """
    biens = []
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        lignes = f.readlines()
        if not lignes:
            return biens
        en_tete = lignes[0].strip().split(',')
        for ligne in lignes[1:]:
            if nb_elements is not None and len(biens) >= nb_elements:
                break
            valeurs = ligne.strip().split(',')
            if len(valeurs) != len(en_tete):
                continue  
            bien = {col: val for col, val in zip(en_tete, valeurs)}
            biens.append(bien)
    return biens 