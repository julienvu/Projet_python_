#projet pizza liste

def tri_personnalise(e):
    return len(e)#tri longueurs de chaines


def afficher(collection, n_premiers_elements= -1):
    #"---- Liste des pizzas"
    #afficher les pizzas 1 pizza par ligne
    #collection.sort(reverse=True,key=tri_personnalise)#tri personnalité différent de reverse pour sort
    c=collection
    if not (n_premiers_elements == -1) :
        c=collection[0:n_premiers_elements]
    nb_pizzas=len(c)
    if nb_pizzas==0:
        print("Aucune Pizza")
        return 
    print(f"--------- Liste des pizzas({nb_pizzas}) ")
    for pizza in c:
        print(pizza)
    print()
    print("Première pizza: ", collection[0])
    print("Dernière pizza: ", collection[-1])
    

#afficher(pizzas)

"""def pizza_existe(e, pizzas):
    for i in pizzas:
        if i==e:
            return True
    return False
"""        

def ajouter_pizza_utilisateur(pizzas):
    pizza_ajout=input("Pizza à ajouter: ")
    if pizza_ajout.lower() in pizzas: #sensibilité à la casse
        print("Erreur: la pizza existe déjà")
    else:
        pizzas.append(pizza_ajout)    
    

vide=()
#afficher (vide)


pizzas=["4 fromages", "végétarienne", "hawai", "calzone"]
#ajouter_pizza_utilisateur(pizzas)
afficher(pizzas, 3)

#s="Bonjour"
#print(s.lower())
#print(s.upper())
#lower() - > minuscules
#upper() - > majuscules




