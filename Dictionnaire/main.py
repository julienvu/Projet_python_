#Dictionnaire

personne = { 'nom': 'Mélanie', "age": 25, "taille": 1.60}
print(personne)

print(personne['nom'])
print(personne['age'])


personne['nom']= "Claire"
print(personne)

personne['poste']= "Développeur"
print(personne)

achat = ("Chocolat", "beurre", "frommage")
personne['achat']=achat
#print(personne)

for i in personne:
    print(f"clef: {i} - valeur: {personne[i]}")
    print(personne[i])
    


#------------- Partie 2-------------------
#dictionnaire: collection puissance

# noms age, taille
#attention mettre des parenthèses pas des crochets
personnes = [
    ("Mélanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65)    
    
]
def obtenir_informations(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

# Jacques

#Jacques

#infos = obtenir_informations("Jacques", personnes)
#print(infos)

personnes_dict = {
    "Mélanie": (25, 1.6),
    "Paul" : (29, 1.8),
    "Jacques": (35, 1.75),
    "Martin": (16, 1.65)    
}
#dictionnaire : nombre important de données boucles
infos = personnes_dict.get("Jacques")
if not infos:
    print("la clef n'existe pas")
else:
    print("La clé existe:")
    print(infos)
    

