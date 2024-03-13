# les fonctions
"""
nom = "toto"
#Même affichage sur la console mais une différence majeure
print("Je m'appelle " + nom)#concaténer une chaine on passe un paramètre
print()
print("Je m'appelle", nom, "j'ai", 30, "ans")#on passe deux paramètres
"""

def est_majeur(age:int) :
    #vrai ou faux (True)
    #si l'âge >=18 => True sinon False
    if age<=0:
        return False
    if age >=18:
        return True
    return False
"""recuperer_et_afficher_infos_personne

   -> recuperer_infos_personne()
   ->afficher_infos_personne(nom,age)
      -> est_majeur()

"""


def recuperer_infos_personne(numero_personne):
    nom_personne= input("Nom de la personne : "+ str(numero_personne) + ": ")
    age_personne= input("Age de la personne : "+ str(numero_personne) + ": ")
    return nom_personne,int(age_personne)

def afficher_infos_personne(numero_personne,nom,age:int):
    print("La personne", numero_personne, "est", nom, "son âge est", age, "ans")
    print("Le nom comporte", len(nom), "lettres")
    if est_majeur(age):
            print("Il est Majeur")
    else:
        print("Il est mineur")

#Implémenter RecupererEtAfficherInfosPersonne
#parametre: numero_personne
#rien retourner
#input/print

#1 seul paramètre pas 2 paramètres
def RecupererEtAfficherInfosPersonne(numero_personne):
    nom,age=recuperer_infos_personne(numero_personne)
    afficher_infos_personne(numero_personne,nom,age)
   
    
    
nb_personnes= 2

for i in range (nb_personnes): #0    
    RecupererEtAfficherInfosPersonne(i+1)#commencer à 1 pas à 0
    
    
afficher_infos_personne("007","James Bond",23)

"""input("Votre nom :")#retourne une valeur
print("Votre nom est:" , nom)
"""
"""
nom1= input("Nom de la personne 1: ")
age1= input("Age de la personne 1: ")
print("La personne 1 est", nom1, "son âge est", age1, "ans")
print("Le nom comporte", len(nom1), "lettres")

nom2= input("Nom de la personne 2: ")
age2= input("Age de la personne 2: ")
print("La personne 2 est", nom2, "son âge est", age2, "ans")
print("Le nom comporte", len(nom2), "lettres")
"""
"""




#définition fonction (juste s'il existe)
#age : paramètre optionnel égal à 0
def afficher_infos_personne(nom="", age=0):
    if nom== "":
        print("Vous n'aviez pas donné de nom, l'age vaut", age)
        return 
    if age==0:
        print("La personne est", nom)
    else:   
        print("La personne est", nom+ ", son age est", age, "ans")
    majeur_ou_non= est_majeur(age)
    if majeur_ou_non:
        print("est majeur")
    else: 
        print("Mineur")
    print("Le nom comporte", len(nom), "caractères")
    
print("Début du programme")
#exécuter fonction rentrer dans la fonction
#afficher_infos_personne("toto",45)
#afficher_infos_personne("emilie")
#error: pas de len(0) sur nom
afficher_infos_personne(age=0)
age=0
if age ==0 :
    exit(0)

majeur_ou_non= est_majeur(age)
if majeur_ou_non:
    print("est majeur")
else: 
    print("Mineur")
print("Fin du programme")
#le def pas exécuté en premier mais mémorise
"""


