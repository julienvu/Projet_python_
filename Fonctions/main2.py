#Fonctions récursives

"""def a(n, limit):
    
    if n > limit:
        return
    print("n: ", n)
    a(n*n, limit)
    
    #boucle infini : accumulation de fonctions très longue hiérarchie très longue
a(2, 100000)
"""
"""
def demander_choix_utilisateur(min,max):
    reponse_str= input("Quel est votre choix entre"+ str(min)+ " et "+ str(max)+ " :")
    try:
        reponse_int=int(reponse_str)
        if not min <= reponse_int<=max:
            print("vous devez rentrer un nombre entre", min, " et", max) 
            return demander_choix_utilisateur(min,max) 
            
        return reponse_int         
    except:
        print("ERREUR: Vous devez rentrer un nombre")
        return demander_choix_utilisateur(min,max)
        
choix=demander_choix_utilisateur(1,4)
print(choix)
"""


#différence break et return

def a():
    print("Début de la fonction")
    for i in range(0,100):
        if i >20:
            break#différence sortir de la boucle mais pas de la fonction et continuer la boucle
            #return : sortir de la fonction 
        
        print(i)
    print("Fin de la fonction")
    
    
#a()


#call back
"""
def ma_fonction():
    print("toto")
    return 1

a=5

b=ma_fonction()

print("a", a, "b", b)
"""

        
def mult_callback(a,b):
    return a*b
def mult_callback(a,b):
    return a+b   



def power_callback(a,b):
    return pow(a,b)          

def afficher_table(n, operateur_str, operation_callback):
    for i in range(1,10):
        
        print(i, operateur_str, n, "=", operation_callback(i,n))
        
    
#afficher_table_multiplication(2)

#afficher_table_addition(2)

#afficher_table(2,"*",mult_callback)
#option 2 avec lambda
#afficher_table(2,"*",lambda a,b: a*b)

#print()
#afficher_table(2,"+",mult_callback)
#option 2 avec lambda
#afficher_table(2,"*",lambda a,b: a+b)
#print()
#afficher_table(2,"^",power_callback)
#option 2 avec lambda
#afficher_table(2,"*",lambda a,b: a^b)


#nombre bariable de paramtres


"""def a(age, taille, numero_telephone):
    print("toto")
    
    
a(20,1.75,"0612343454")"""

#nombre variable de paramètres
#récolter toutes les valeurs
def somme(titre,*nombres):
    print("Titre",titre)
    resultat=0
    for n in nombres:
        resultat+=n
    return resultat
print(somme("somme des points", 15, 11, 18))
