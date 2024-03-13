import time
import random
import os


"""

- Longueur séquence initiale: 4
- Durée de mémorisation: 3s
- A chaque tour: 1 chiffre
- Un nombre de vies

Facile
    longueur_initiale: 3
    duree_memorisation: 4
    increment_sequence: 1
    nombre_vies: 2

Normal
    longueur_initiale: 4
    duree_memorisation: 3
    increment_sequence: 1
    nombre_vies:1

Difficile
    longueur_initiale: 5
    duree_memorisation: 2
    increment_sequence: 2
    nombre_vies: 0
"""

#Dictionnaire un tuple niveaux_difficulté
NIVEAUX_DIFFICULTE= (
    
    {
        "titre": "Facile",
        "longueur_initiale":3,
        "duree_memorisation_sec": 4,
        "increment_sequence": 1,
        "nombre_essais": 3,
    
    },
    {
        "titre": "Normal",
        "longueur_initiale":4,
        "duree_memorisation_sec": 3,
        "increment_sequence": 1,
        "nombre_essais": 2,
        
    }, 
    {
        "titre": "Difficile",
        "longueur_initiale":4,
        "duree_memorisation_sec": 3,
        "increment_sequence": 1,
        "nombre_essais":1,
    },
) 



# Fonction pour effacer l'écran
def clear_screen():
    if(os.name =="posix"):
        os.system("clear")
    else:
        os.system("cls")


def demander_valeur_numerique_min_max(nb_min,nb_max):
    #quel est le nombre magique entre 1 et 10
    #conversion str en int (variable intermédiaire)
    #cas erreur nombre invalide ou hors des bornes (nb_min et nb_max)
    nombre_int=0
    while nombre_int==0:
        nombre=input("Quel est le nombre magique (entre " + str(nb_min) + " et " + str(nb_max) + " )?" )
        try:
            nombre_int=int(nombre)
        except:
            print("ERREUR: Vous devez taper un nombre. Réessayez")
        #problème intervalle de valeur
        else:
            if nombre_int > nb_max or nombre_int < nb_min:
                print(f"ERREUR: Le nombre doit être entre {nb_min} et {nb_max} . Réessayez")
                #remttre nombre_int à 0 pour retaper un autre nombre et ne pas sortir de la boucle
                nombre_int=0
    return nombre_int


def choix_niveaux_difficulte(niveaux_difficulte):
    print("Choisissez votre niveau")
    index = 1
    for niveau in niveaux_difficulte:
        print(f"{index} - {niveau["titre"]}")
    choix=demander_valeur_numerique_min_max(1, len(niveaux_difficulte))
    return niveaux_difficulte[choix-1]


def generer_sequence(n):
# séquence de départ
# Pour chaque nombre dans la séquence de départ ont les génère d'une façon aléatoire
    sequence = ("")
    for i in range(4):
        nombre = random.randint(0, 9)
        sequence += str(nombre)
    return sequence



#choix niveau de difficultés
niveau_difficulte_dict=choix_niveaux_difficulte(NIVEAUX_DIFFICULTE)

#générer séquence initiale
sequence=generer_sequence(niveau_difficulte_dict["longueur_initiale"])


nombre_essais_restants= niveau_difficulte_dict["nombre_essais"]


# titre du programme
clear_screen()
print("")
titre="Bienvenue dans le jeu du Simon "
l=len(titre)+16
print("*"*l)
print("        "+titre+" ")
print("*"*l)

"""--------------------------------------------- Programme Principal --------------------------------------------"""

# score de départ
score = 0

""" création de la boucle
 sur la répétion de la séquence a afficher 
 et demander a l'utilisateur d'entrer sa réponse """

while True:
    print("")
    print("Retenez la séquence")
    time.sleep(1)
    print(sequence)
    time.sleep(niveau_difficulte_dict["duree_memorisation_sec"])
    clear_screen()
    
    
    print(f"Nombre essais restants: {nombre_essais_restants}")
    print(f"Vorte score: {score}")
    print("")
    reponse_joueur = input("Entrer votre réponse ")

    # incrémentation du score si bonne réponse
    if reponse_joueur == sequence:
        score += 1
        sequence += generer_sequence(niveau_difficulte_dict["increment_sequence"])
        print("Bonne réponse")
    else:
        nombre_essais_restants -=1
        if nombre_essais_restants < 0 :
            break
        print("Mauvaise réponse, réessayez")
    
    
    clear_screen()

# reponse possible en fonction du score
print("")
print(f"la bonne séquence était {sequence} votre avez un score de : {score} ")
print("")
