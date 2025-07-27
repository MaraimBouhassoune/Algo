
"""
Implémentation des 4 algorithmes de tri :
  • Sélection   • Insertion
  • Fusion      • Rapide (pivot aléatoire)

Chaque fonction renvoie :
    (liste triée, nb_comparaisons, nb_échanges|décalages, temps_sec)
"""

from time import perf_counter as _now
from random import randint


# --------------------------------------------------------------------------- #
def tri_selection(lst, key):
    t0 = _now()
    tab = lst.copy()
    n = len(tab)
    comp = exch = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if float(tab[j][key]) < float(tab[min_idx][key]):
                min_idx = j
        if min_idx != i:
            tab[i], tab[min_idx] = tab[min_idx], tab[i]
            exch += 1
    return tab, comp, exch, _now() - t0


# --------------------------------------------------------------------------- #
def tri_insertion(lst, key):
    t0 = _now()
    tab = lst.copy()
    comp = shift = 0

    for i in range(1, len(tab)):
        pivot = tab[i]
        j = i - 1
        while j >= 0 and float(tab[j][key]) > float(pivot[key]):
            comp += 1
            tab[j + 1] = tab[j]
            shift += 1
            j -= 1
        comp += 1                      
        tab[j + 1] = pivot
        if j + 1 != i:
            shift += 1
    return tab, comp, shift, _now() - t0


# --------------------------------------------------------------------------- #
def tri_fusion(lst, key):
    t0 = _now()
    comp = [0]

    def _merge(a, b):
        res, i, j = [], 0, 0
        while i < len(a) and j < len(b):
            comp[0] += 1
            if float(a[i][key]) <= float(b[j][key]):
                res.append(a[i]); i += 1
            else:
                res.append(b[j]); j += 1
        res.extend(a[i:]); res.extend(b[j:])
        return res

    def _sort(tab):
        if len(tab) <= 1:
            return tab
        m = len(tab) // 2
        return _merge(_sort(tab[:m]), _sort(tab[m:]))

    return _sort(lst.copy()), comp[0], _now() - t0


# --------------------------------------------------------------------------- #
def tri_rapide(lst, key):
    t0 = _now()
    tab = lst.copy()
    comp = [0]
    exch = [0]

    def _partition(lo, hi):
        p = randint(lo, hi)           
        tab[p], tab[hi] = tab[hi], tab[p]
        exch[0] += 1

        pivot = float(tab[hi][key])
        i = lo - 1
        for j in range(lo, hi):
            comp[0] += 1
            if float(tab[j][key]) <= pivot:
                i += 1
                if i != j:
                    tab[i], tab[j] = tab[j], tab[i]
                    exch[0] += 1
        if i + 1 != hi:
            tab[i + 1], tab[hi] = tab[hi], tab[i + 1]
            exch[0] += 1
        return i + 1

    def _quicksort(lo, hi):
        if lo < hi:
            p = _partition(lo, hi)
            _quicksort(lo, p - 1)
            _quicksort(p + 1, hi)

    _quicksort(0, len(tab) - 1)
    return tab, comp[0], exch[0], _now() - t0
