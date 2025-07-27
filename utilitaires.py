"""
Lecture robuste du CSV : renvoie une liste de dictionnaires.
Gère les virgules dans les données et la conversion des types.
Aucune bibliothèque externe.
"""

def lire_csv_biens(path, n_max=None):
    """
    Lit le fichier CSV et retourne une liste de dictionnaires.
    Gère correctement les virgules dans les données.
    """
    biens = []
    
    try:
        with open(path, encoding="utf-8") as f:
            lignes = f.readlines()
    except FileNotFoundError:
        print(f"Erreur : fichier {path} non trouvé")
        return biens
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier : {e}")
        return biens

    if not lignes:
        return biens

  
    header = lignes[0].strip().split(',')
    
    for i, line in enumerate(lignes[1:], 1):
        if n_max is not None and len(biens) >= n_max:
            break
            
        line = line.strip()
        if not line:  
            continue
            
       
        vals = parse_csv_line(line)
        
        if len(vals) != len(header):
            print(f"Ligne {i+1} ignorée : nombre de colonnes incorrect ({len(vals)} vs {len(header)})")
            continue
            
       
        bien = {}
        for j, (key, val) in enumerate(zip(header, vals)):
            bien[key] = convert_value(val, key)
        
        biens.append(bien)
    
    print(f"✅ {len(biens)} biens immobiliers chargés depuis {path}")
    return biens


def parse_csv_line(line):
    """
    Parse une ligne CSV en gérant les virgules dans les valeurs.
    """
    vals = []
    current_val = ""
    in_quotes = False
    
    i = 0
    while i < len(line):
        char = line[i]
        
        if char == '"':
            in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            vals.append(current_val.strip())
            current_val = ""
        else:
            current_val += char
        i += 1
    
 
    vals.append(current_val.strip())
    return vals


def convert_value(value, key):
    """
    Convertit une valeur selon le type attendu pour la clé donnée.
    """
    value = value.strip().strip('"')  
    
    if not value:
        return value
    
    
    if key in {"prix", "surface", "nb_pieces", "code_postal"}:
        try:
            return int(float(value))  
        except (ValueError, TypeError):
            return value
    
  
    elif key in {"prix_m2"}:
        try:
            return float(value)
        except (ValueError, TypeError):
            return value
    
    
    else:
        return value


def afficher_statistiques_dataset(biens):
    """
    Affiche des statistiques sur le dataset chargé.
    """
    if not biens:
        print("❌ Aucune donnée à analyser")
        return
    
    print(f"\n📊 STATISTIQUES DU DATASET")
    print(f"   • Nombre total de biens : {len(biens)}")
    
    
    types = {}
    for bien in biens:
        t = bien.get('type_local', 'Inconnu')
        types[t] = types.get(t, 0) + 1
    
    print(f"   • Répartition par type :")
    for type_bien, count in sorted(types.items()):
        print(f"     - {type_bien} : {count}")
    
   
    prix_valides = [bien['prix'] for bien in biens if isinstance(bien['prix'], (int, float))]
    if prix_valides:
        print(f"   • Prix : {min(prix_valides):,}€ → {max(prix_valides):,}€")
    
   
    surfaces_valides = [bien['surface'] for bien in biens if isinstance(bien['surface'], (int, float))]
    if surfaces_valides:
        print(f"   • Surface : {min(surfaces_valides)}m² → {max(surfaces_valides)}m²")
    
    print()


def valider_donnees(biens):
    """
    Valide la cohérence des données chargées.
    """
    if not biens:
        return False
    
    erreurs = 0
    
    for i, bien in enumerate(biens):
       
        champs_requis = ['prix', 'surface', 'type_local', 'commune']
        for champ in champs_requis:
            if champ not in bien or not bien[champ]:
                print(f"⚠️  Bien {i+1} : champ '{champ}' manquant")
                erreurs += 1
        
        
        if isinstance(bien.get('prix'), (int, float)) and bien['prix'] <= 0:
            print(f"⚠️  Bien {i+1} : prix invalide ({bien['prix']})")
            erreurs += 1
            
        if isinstance(bien.get('surface'), (int, float)) and bien['surface'] <= 0:
            print(f"⚠️  Bien {i+1} : surface invalide ({bien['surface']})")
            erreurs += 1
    
    if erreurs == 0:
        print("✅ Toutes les données sont valides")
        return True
    else:
        print(f"❌ {erreurs} erreur(s) détectée(s) dans les données")
        return False