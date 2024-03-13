#collections: {Tableaux: Array} , liste, tuples
#tuple(): immutable - > non modifiable
#liste: mutable: peut être modifié ajout/suppression éléments ou modification éléments



a=5
b="toto"

personnes = ("Mélanie", "Jean" , "Martin" , "Alice")#à lecture seul pour le tuple
#print(len(personnes))
#print(personnes[0]) #premier élément à l'index 0
#print(personnes[-1])#tuple: Alice dernier élément particularité de Python 
#print(personnes[-2])#avant-dernier élément Martin
#for i in range(0, len(personnes)):
#    print(personnes[i])


#for i in personnes:
#    print(i)
#    print(len(i))#longueur de chaque élément du tuple
#    print(i[0])#première lettre affichée


#(0,1,2,3,4)
#valeurs = range (0,10)
#print(valeurs[-1]) affiche 9 dernier élément

#personnes = ["Mélanie", "Jean" , "Martin" , "Alice"]
#nouvelle_personne = "David"

#print(personnes)

#personnes.append(nouvelle_personne)
#del personnes[1]
#print(personnes)

def afficher_personnes(c):
    for i in c:
        print(i)
        
def modifier_valeur(a):
        a[0]=10
    
test= [1, 2, 3, 4]
#print(test)
#modifier_valeur(test)
#print(test)#5 recréer une variable locale a à la fonction mais différente de la variable globale test
#liste: conteneur --- > modifier les valeurs de ce conteneur
#liste remplacer premier élément de cette liste




# -------------- Fonctions et tuples -----------------


def obtenir_informations ():
    return "Mélanie", 37, 1.68

def afficher_informations(nom, age, taille):
    print(f" Informations : Nom: {nom}, age: {age}, taille:{taille}")



#infos= obtenir_informations()
#afficher_informations(*infos)#manque 2 paramètres avec l'étoile ça paramètre les arguments du tuple
#infos= obtenir_informations()
#print("nom: " + infos[0])
#print("age: " + str(infos[1]))
#print("taille: "+ str(infos[2]))

#nom, age, taille =obtenir_informations()
#afficher_informations(nom,age,taille)

#print(infos)
#print(*infos)#unpack le tuple déballer fractionnement




#---------- Slices -------------


personnes = ("Mélanie", "Jean" , "Martin" , "Alice", "Pierre", "Paul")


#[start:stop:step] slice 


#for i in personnes[::2]:
#    print(i)

nom="Jean"

print(nom[::-1])#jean en inversé


