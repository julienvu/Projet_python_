#collections: listes/tuples
#append/extend/ += / Insert


noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"] #liste
#noms_supplementaires = []

#noms.append(noms_supplementaires) #ajoute un item à la liste

#for e in noms_supplementaires:
#    noms.append(e)
#noms.extend(noms_supplementaires) #plusieurs éléments concaténation
#noms+=noms_supplementaires   

#noms.insert(1, "Toto") 

#noms=noms_supplementaires + noms

slices_noms= noms[-2:]# avec [:]: recopie les valeurs  nouvelle copie des mêmes valeurs de noms
#on se retrouve avec 2 listes
#slice: créer une nouvelle liste
#slices_noms[0]= "Toto"

def tri_longueur_caracteres(nom):
    return len(nom)

#print(noms[1:])
#print(slices_noms)
#print(noms)


#tri/sort/sorted
#tri personnalité
#noms.sort(key= tri_longueur_caracteres, reverse=True) #inplace 


#noms_Tries=sorted(noms, reverse=True)
#print(noms)

ages=[21, 20, 30, 25,22]

#print(max(ages))# sur des valeurs numériques pas des chaines de caractères

#opérateur in contenu dans la liste
'''if 31 in ages:
    print("Présent")
else:
    print("Absent")
'''

'''
found=False
for nom in noms:
    if nom == "Martin":
        print("Présent")
        found=True
        break
if found:
    print("Présent")
else:
    print("Abscent")
'''

#print(sum(ages))#uniquement sur des collections avec des valeurs numériques

#swapper deux élémens d'une liste
'''
t=noms[0]#Jean
noms[0]=noms[4]#Jean=Zoe
noms[4]=t
#pas marché car variable écrasée
'''



#autre solution envisagée autant de variables que de variables à changer/attribuer
#noms[1], noms[3]= noms[3], noms[1]



#join : rejoindre - > coller 
#split: séparer


#noms_join = ", ".join(noms)

#print(noms_join)

# split: Séparer
#a="Paul, Marc, Emilie"

#noms_recons=noms_join.split(", ")
#print(noms_recons)

#element_cherche="Martin"
#nb_occurences= noms.count(element_cherche)
#print(nb_occurences)
'''
if nb_occurences > 0:
    index_occurence=0
    for i in range(nb_occurences):
        index_occurence=noms.index(element_cherche,index_occurence)#martin à l'index 2 l'index de la première valeur
        print(element_cherche, "trouvé à ", index_occurence)
        index_occurence+=1
        

else:
    print(element_cherche+ "n'est pas dans la collection. ")# pas dans la liste



'''
#find pour les chaines de caractères pas sur la liste (collections)
'''
a="Jean-Martin-Toto"
i= a.find("martin")
print(i)
'''

#liste longueur des caractères

longueur_noms= [len(nom) if len(nom)<10 else 0 for nom in noms]
#longueur_noms = [len(nom) for nom in noms]#compréhension des listes
#print(longueur_noms)

#noms_avec_E= [nom for nom in noms if "e" in nom]#condition avec les mots avec des E

#print(noms_avec_E)
'''
for nom in noms:
    longueur_noms.append(len(nom))
    
    print(longueur_noms)
''' 
#a=[i for i in range(5) if (i//2)*2== i]#0,2,4 éléments paires
#print(a)


b=[True if (i//2)*2==i else False for i in range(11)]#éléments paires avec True

#print(b)


#oooléen

'''
a=[True, True, True, True]

print(any(a))#éléments de a au moins trouvé un seul true
print(all(a))#false pas tous les éléments à True
'''
'''
found= False
for nom in noms:
    if "z" in nom.lower():
        found=True
        print("Trouvé")
        break
    
if found:
    print("Trouvé")
else:
    print("Non trouvé")
'''   
    
noms_avec_un_z=[True if "e" in nom.lower() else False for nom in noms]
#print(any(noms_avec_un_z))#True
#print(all(noms_avec_un_z))#False

'''
print("a".isdigit())#pas un chiffre False
print("9".isdigit())#un chiffre
'''


'''
def chaine_contient_chiffre (chaine):
    """for c in nom:
        if c.isdigit():
            return True
    return False """ 
    return any([c.isdigit() for c in chaine])  

nom = "toto"
print(chaine_contient_chiffre(nom))#pas de chiffre false
'''
'''
nom= input("Quel est ton nom ? " )
if nom== "":
    print("Le nom est vide")
elif chaine_contient_chiffre(nom):
    print("nom invalide pas contenir de chiffres")
else:
    print("Bonjour" + nom)


nom= "toto12"
contient_un_chiffre= any([c.isdigit() for c in nom])  
print(contient_un_chiffre)#true
'''


def element_dans_liste(e,l):
    '''for el in l:
        if e.lower() == el.lower():
            return True
    return False'''
    l_lower= [el.lower() for el in l]
    return e.lower() in l_lower
'''
if element_dans_liste("JEAN", noms):
    print("Jean est là")
else:
    print("Jean n'est pas là")
'''

fichiers=("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc","Document Word"),
                        ("exe", "Executable"),
                        ("txt", "Document Texte"),
                        ("jpeg", "Image JPEG"))

definition_extensions_dict= {"doc":"Document Word",
                             "exe": "Executable",
                             "txt": "Document Texte",
                             "jpeg": "Image JPEG"
    
}

'''
notepad.exe (Executable)
mon.fichier.perso.doc (word)
notes.TXT(document Texte)
vacances.jpeg (Image JPEG)
planning (Aucune extension)
data_dat (Extension non connue)
'''    

#lower/upper
#in/index/for
#split
#-1


#extraire l'extension du fichier
#faire la correspondance avec definition_extensions
def extraire_extension(nom_fichier):
    nom_fichier_split=nom_fichier.split(".")
    if len(nom_fichier_split) > 1:
        return (nom_fichier_split[-1])
    return None

def obtenir_definition_extension(extension, definitions):
    for d in definitions:
        if d[0].lower() == extension.lower():
            return d[1]
    return None

'''
for fichier in fichiers:
    ext=extraire_extension(fichier)
    if ext:
        definition= obtenir_definition_extension(ext, definition_extensions)
        #definition= definition_extensions_dict.get(ext.lower())
        if not definition:
            definition="Extension non connue"
    else:
        definition= "Aucune extension"
    print(fichier + " ("+definition+ ")")    
'''


#nombre total de carachtères

# 1 - for/len

'''   
s=0
for nom in noms:
        s+= len(nom)
        
        print("Nombre total de caractères", s)'''

#2 complétion de liste+ sum

#liste + sum
longueur_noms= [len(nom) for nom in noms]
#print("nombre total de caractères:", sum(longueur_noms))#35



#join/len concaténer (moins de mémoire valeurs compteur)
tous_les_noms="".join(noms)#pas prendre les virgules
#print(len(tous_les_noms))#35 join



#fonctions zip
#liste en une seule forme de tuples


pizzas_nom = ("4 fromages", "Calzone", "Hawai")

pizzas_prix = (10.5, 11, 8)
noms_et_prix=list(zip(pizzas_nom, pizzas_prix))
#print(noms_et_prix)

for (nom,prix) in zip(pizzas_nom, pizzas_prix):
    print(f"{nom} - {prix} £")


unzipped= list(zip(*noms_et_prix))
#print(unzipped)

set_noms= list(set(noms))
#print(set_noms)#set table de hachage


set_noms= {"Marie", "Marie", "Jean","Marc","Emilie"}
for s in set_noms:
    print(s)






