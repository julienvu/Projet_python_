

#nom1 = input("Quel est ton nom?")
#age=input("Quel est votre âge?")# un seul paramètre possible avec input

#nom1="toto"
#age=19

#gestion erreurs et exceptions try except else


#try:
    #age_prochain = int(age)+1
#except ValueError:
    #plusieurs paramètres pour print possible
    #print("ERREUR: Vous devez rentrer un nombre pour l'age")

#else:    
    #print("Vous vous appelez toto, vous avez "+ str(age)+ " ans") # pas de conversion un nombre en châine de caractères
    #pas de concaténation d'entiers mais seulement des chaînes de caractères
    #print("l'an prochain vous aurez  "+ str(age_prochain) + " ans")


n=0
#print(n)
#n=10
#print(n)
#n=n+1
#print(n)
#boucle infinie

#print ("début de la boucle")
#while n < 10:
 #   print("Valeur de n:  "+ str (n))
#    n=n+1
    
#print("fin de la boucle")


#mot_de_passe= ""
#while not mot_de_passe== "TOTO" :
 #   mot_de_passe= input ("Quel est le mot de passe ? ")

#print("Mot de passe correct, vous avez accès au compte")
#demander_nom
#reponse_nom
#return reponse_nom


#afficher_informations_personne(nom,age)
#nom,age print
def afficher_informations_personne(nom,age,taille=0):
    print()
    #sans accolades
    print("Vous vous appelez "+nom, "vous avez "+ str(age)+ " ans")
    #avec les accolades print
    print(f"Vous vous appelez {nom}, vous avez {age} ans")
    print(f"l'an prochain vous aurez  "+ str(age+1) + " ans")
    print("l'an prochain vous aurez %s ans " % (age+1))   
    
    # == egal
    # < inférieur
    #<= inférieur ou égal
    #>= supérieur ou égal
    #condition= age >=18
    
    #print(condition)
    #if condition:
        
    #    print("Vous êtes majeur")
    #else :
    #    print("Vous êtes mineur")
    
    
    if age ==17:
        print("Vous êtes presque majeur")
    elif 12 <= age <=18 :
        print("Vous êtes adolescent")
    elif age==1 or age==2:
        print("Vous êtes un bébé")
    if age ==18:
        print("Tout juste majeur: félicitation")
    elif age>60:
        print("Vous êtes senior")
    elif age < 18:
        print("Vous êtes enfant")
    elif age >=18:
        print("Voutes êtes majeur")
        
        
    #afficher la taille
    if not taille ==0:
        print("Votre taille "+ str(taille) + " m")

def demander_nom():
    reponse_nom=""
    while reponse_nom=="":
        reponse_nom=input("Quel est votre nom ? ")
    return reponse_nom
def demander_age(nom_personne):
    age_int=0
    while age_int==0:
        age_str=input(nom_personne + " Quel est votre âge ? ")
        try:
            age_int=int(age_str)
        except ValueError:
            print("ERREUR: Vous devez rentrer un nombre pour l'age")   
    return age_int       

#personnes nom
#nom1=demander_nom()
#nom2=demander_nom()

#âge personnes
#age1=demander_age(nom1)
#age2=demander_age(nom2)

#appel afficher_informations_personne
#afficher_informations_personne(nom1,age1)
#afficher_informations_personne(nom2,age2)


#print("Vous vous appelez "+nom1, "vous avez "+ str(age1)+ " ans")
#print("l'an prochain vous aurez  "+ str(age1+1) + " ans")  

#print("Vous vous appelez "+nom2, "vous avez "+ str(age2)+ " ans")
#print("l'an prochain vous aurez  "+ str(age2+1) + " ans")  

#valeur constante NB_PERSONNES
NB_PERSONNES =3 

#boucle
for i in range (0, NB_PERSONNES):
    nom= "personne" + str(i+1)
    age=demander_age(nom)
    #3 paramètres dans la fonction d'affichage
    afficher_informations_personne(nom,age, 1.60)


#print sur plusieurs lignes

print("""
      
Vous mettez ce que vous voulez
      
      
  """
)
print("toto", 20, "ans", "taille:", 1.78)




#approche visuelle



#module
#turtle (triangle) haut du triangle 4 commandes forward: avancer
#backward
#right (90)
#left (90)



