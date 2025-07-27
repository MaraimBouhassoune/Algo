
"""
3 algorithmes de recherche :
  • Linéaire (compte ou position)
  • Binaire
  • Min/Max (un seul parcours)

Chaque fonction renvoie comparaisons + temps
"""

from time import perf_counter as _now


def _num(v, k):
    if isinstance(v, (int, float)):
        return v
    try:
        return int(v) if k in {"prix", "surface", "nb_pieces"} else float(v)
    except (ValueError, TypeError):
        return v


# --------------------------------------------------------------------------- #
def recherche_lineaire(table, predicate):
    found = comp = 0
    t0 = _now()
    for elt in table:
        comp += 1
        if predicate(elt):
            found += 1
    return found, comp, _now() - t0


def recherche_lineaire_position(table, cible, key):
    comp = 0
    t0 = _now()
    for i, elt in enumerate(table):
        comp += 1
        if _num(elt[key], key) == cible:
            return i, comp, _now() - t0
    return -1, comp, _now() - t0


# --------------------------------------------------------------------------- #
def recherche_binaire(sorted_table, cible, key):
    g, d = 0, len(sorted_table) - 1
    comp = 0
    t0 = _now()
    while g <= d:
        m = (g + d) // 2
        val = _num(sorted_table[m][key], key)
        comp += 1
        if val == cible:
            return m, comp, _now() - t0
        if val < cible:
            g = m + 1
        else:
            d = m - 1
    return -1, comp, _now() - t0


# --------------------------------------------------------------------------- #
def recherche_min_max(table, key):
    if not table:
        return None, None, 0, 0.0
    vmin = vmax = _num(table[0][key], key)
    comp = 0
    t0 = _now()
    for elt in table[1:]:
        v = _num(elt[key], key)
        comp += 1
        if v < vmin:
            vmin = v
        comp += 1
        if v > vmax:
            vmax = v
    return vmin, vmax, comp, _now() - t0
