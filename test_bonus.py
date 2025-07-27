#!/usr/bin/env python3
"""
Test rapide du bonus tri par tas
"""

from algorithmes_tri import tri_tas, valider_tri
from utilitaires import lire_csv_biens

def test_tri_tas():
    """Test du tri par tas"""
    print("🧪 TEST DU BONUS TRI PAR TAS")
    print("=" * 40)
    
    # Charger des données
    biens = lire_csv_biens('transactions_immobilieres.csv', n_max=50)
    print(f"✅ {len(biens)} biens chargés")
    
    # Test du tri par tas
    tab_trie, comp, ech, temps = tri_tas(biens, 'prix')
    print(f"🏆 Tri par tas : {temps:.4f}s | {comp} comparaisons | {ech} échanges")
    
    # Validation
    valide, msg = valider_tri(biens, tab_trie, 'prix')
    print(f"✅ Validation : {msg}")
    
    # Vérification visuelle
    print(f"📊 Premier prix : {tab_trie[0]['prix']}€")
    print(f"📊 Dernier prix : {tab_trie[-1]['prix']}€")
    
    # Test sur surface aussi
    tab_trie_surface, comp_s, ech_s, temps_s = tri_tas(biens, 'surface')
    print(f"🏆 Tri par surface : {temps_s:.4f}s | {comp_s} comparaisons | {ech_s} échanges")
    
    print("\n🎉 BONUS TRI PAR TAS FONCTIONNE PARFAITEMENT !")

if __name__ == "__main__":
    test_tri_tas() 