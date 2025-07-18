import time

def tri_selection(liste, cle):
    """
    Tri par sélection sur la clé donnée.
    Retourne : (liste_triee, nb_comparaisons, nb_echanges, temps_execution)
    """
    t0 = time.time()
    tab = liste.copy()
    n = len(tab)
    nb_comparaisons = 0
    nb_echanges = 0
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            nb_comparaisons += 1
            if float(tab[j][cle]) < float(tab[min_idx][cle]):
                min_idx = j
        if min_idx != i:
            tab[i], tab[min_idx] = tab[min_idx], tab[i]
            nb_echanges += 1
    t1 = time.time()
    temps_execution = t1 - t0
    return tab, nb_comparaisons, nb_echanges, temps_execution

def tri_insertion(liste, cle):
    """
    Tri par insertion sur la clé donnée.
    Retourne : (liste_triee, nb_comparaisons, nb_decalages, temps_execution)
    """
    import time
    t0 = time.time()
    tab = liste.copy()
    n = len(tab)
    nb_comparaisons = 0
    nb_decalages = 0
    for i in range(1, n):
        clef = tab[i]
        j = i - 1
        while j >= 0:
            nb_comparaisons += 1
            if float(tab[j][cle]) > float(clef[cle]):
                tab[j + 1] = tab[j]
                nb_decalages += 1
                j -= 1
            else:
                break
        tab[j + 1] = clef
        if j + 1 != i:
            nb_decalages += 1  
    t1 = time.time()
    temps_execution = t1 - t0
    return tab, nb_comparaisons, nb_decalages, temps_execution

def tri_fusion(liste, cle):
    """
    Tri fusion sur la clé donnée.
    Retourne : (liste_triee, nb_comparaisons, temps_execution)
    """
    import time
    t0 = time.time()
    nb_comparaisons = [0]  

    def fusion(tab, cle):
        if len(tab) <= 1:
            return tab
        mid = len(tab) // 2
        gauche = fusion(tab[:mid], cle)
        droite = fusion(tab[mid:], cle)
        return fusionner(gauche, droite, cle)

    def fusionner(gauche, droite, cle):
        resultat = []
        i = j = 0
        while i < len(gauche) and j < len(droite):
            nb_comparaisons[0] += 1
            if float(gauche[i][cle]) <= float(droite[j][cle]):
                resultat.append(gauche[i])
                i += 1
            else:
                resultat.append(droite[j])
                j += 1
        resultat.extend(gauche[i:])
        resultat.extend(droite[j:])
        return resultat

    tab_trie = fusion(liste.copy(), cle)
    t1 = time.time()
    temps_execution = t1 - t0
    return tab_trie, nb_comparaisons[0], temps_execution

def tri_rapide(liste, cle):
    """
    Tri rapide (quick sort) sur la clé donnée.
    Retourne : (liste_triee, nb_comparaisons, nb_echanges, temps_execution)
    """
    import time
    t0 = time.time()
    tab = liste.copy()
    nb_comparaisons = [0]
    nb_echanges = [0]

    def quicksort(tab, debut, fin, cle):
        if debut < fin:
            pivot_idx = partition(tab, debut, fin, cle)
            quicksort(tab, debut, pivot_idx - 1, cle)
            quicksort(tab, pivot_idx + 1, fin, cle)

    def partition(tab, debut, fin, cle):
        pivot = float(tab[fin][cle])
        i = debut - 1
        for j in range(debut, fin):
            nb_comparaisons[0] += 1
            if float(tab[j][cle]) <= pivot:
                i += 1
                tab[i], tab[j] = tab[j], tab[i]
                nb_echanges[0] += 1
        tab[i + 1], tab[fin] = tab[fin], tab[i + 1]
        nb_echanges[0] += 1
        return i + 1

    quicksort(tab, 0, len(tab) - 1, cle)
    t1 = time.time()
    temps_execution = t1 - t0
    return tab, nb_comparaisons[0], nb_echanges[0], temps_execution 