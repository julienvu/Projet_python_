import random


#projet nombre aléatoire
#Pratiquer variables numériques boolénnes numériques boucles for/while nombre aléatoire break




def demander_nombre(nb_min,nb_max):
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


NOMBRE_MIN=1
NOMBRE_MAX=10
NOMBRE_MAGIQUE=random.randint(NOMBRE_MIN, NOMBRE_MAX)
nombre=0
NB_VIES=4

vies=NB_VIES

#condition et boucle en dehors de la fonction
#le nombre magique est plus petit 
#le nombre magique est plus grand
#Bravo , vous avez gagnés
#boucle while tant qu'on n'a pas trouvé le nombre magique on tape le nombre en faisant appel à demander_nombre
#boucle while et qu'il reste des vies
"""while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies.")
    #affecter nombre à l'appel de la fonction
    nombre=demander_nombre(NOMBRE_MIN,NOMBRE_MAX) 
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies=vies-1
    else:
        print("Le nombre magique est plus grand")
        vies=vies-1
        
#encore des vies restantes
if vies==0:
    print(f"Vous avez perdu. Le nombre magique était {NOMBRE_MAGIQUE} ")

"""
#variable gagne vrai si on a gagné le jeu
gagne=False
for i in range(0,NB_VIES):
    vies=NB_VIES-i
    print(f"Il vous reste {vies} vies.")
    #affecter nombre à l'appel de la fonction
    nombre=demander_nombre(NOMBRE_MIN,NOMBRE_MAX) 
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        gagne=True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies=vies-1
    else:
        print("Le nombre magique est plus grand")
        vies=vies-1
        
#encore des vies restantes
#if vies==0:
if not gagne:
    print(f"Vous avez perdu. Le nombre magique était: {NOMBRE_MAGIQUE} ")


