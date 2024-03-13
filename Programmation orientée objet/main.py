#programmation orientée objet

#programmation impérative/objet
#la plus simple possible
#exercices, mises en situation


#Personne
#nom,age
#Actions: (méthodes)  
# - SePrésenter()
    #DemanderNom() (input)
    
class EtreVivant:
    ESPECE_ETRE_VIVANT="(être vivant non identifié)"
    def AfficherInfosVivant(self):
        print("Info être vivant "+ self.ESPECE_ETRE_VIVANT)
    
class Chat(EtreVivant):#être vivant classe parent de la classe chat
    ESPECE_ETRE_VIVANT="Chat (Mammifère Félin)"
        
#----Définition ----
class Personne(EtreVivant):
    #variable classe unique à tout le monde
    ESPECE_ETRE_VIVANT="Humain (Mammifère Homo sapiens)"
    #2 tirets pour la fonction constructeur __init__
    def __init__(self, nom:str="", age:int=0):
        self.nom=nom #dans mon objet, stocker variable nom variable d'instance nom variable d'instance au constructeur
        self.age=age
        if nom=="":
            self.DemanderNom()
        print("Constructeur personne "+ self.nom)
    #mettre le self dans paramètre
    def SePresenter(self):
        #self.nom=nom
        info_personne= "Bonjour je m'appelle "+ self.nom
        if self.age != 0:
            info_personne += " , j'ai "+ str(self.age) + " ans" #concaténer info_personne
        print (info_personne) #self.nom variable locale
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")
       
    
    #estMajeur
    #booléen vrai faux self.age
    def EstMajeur(self):
        return self.age >= 18
    
    def DemanderNom(self):
        self.nom=input("Nom de la personne: ")  
        
#EtreVivant
#Personne
#etudiant      
        
        
class Etudiant(Personne):
    #variable classe unique à tout le monde
    #2 tirets pour la fonction constructeur __init__
    def __init__(self, nom:str="", age:int=0, etudes:str=""):
        #self.nom=nom #dans mon objet, stocker variable nom variable d'instance nom variable d'instance au constructeur
        #self.age=age
        self.etudes= etudes
        super().__init__(nom,age)#surcharge (réutilisation de la méthode classe personne)
    def SePresenter(self):
        super().SePresenter()#surcharge réutilisation de la méthode classe personne
        print("Je suis étudiant en " + self.etudes)
    ##self.nom=nom
        '''info_personne= "Bonjour je m'appelle "+ self.nom
        if self.age != 0:
            info_personne += " , j'ai "+ str(self.age) + " ans" #concaténer info_personne
        print (info_personne) #self.nom variable locale
        if self.age !=0:
            if self.EstMajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur.")'''
#2 mémoires
#---- UTILISATION ----
#Méthode d'instance (différentes objets)
#personne1= Personne("Jean", 30)#Je cree une personne
#personne2= Personne("Paul", 15)#Je cree une personne #méthodes d'instances

liste_personnes=[Personne("Jean", 30), Personne("Paul", 15), Personne("Zoe", 20)]
#liste_personnes[1].SePresenter()
#personne4=Personne(age=20)
#liste_personnes.append(personne4)

#Altérer la variable de la première instance
#3 instances au total

#Personne.espece_etre_vivant="Mutant"#variable de classe
liste_personnes[0].ESPECE_ETRE_VIVANT="Mutant"


print("Affichage liste")
for personne in liste_personnes:
    personne.SePresenter()
    personne.AfficherInfosVivant()
    print()
    
    
    

#personne1.SePresenter()
#personne2.SePresenter()
#personne3= Personne(age=20)
#personne3.SePresenter()
#print("estMajeur1 :", personne1.EstMajeur())
#print("estMajeur2 :", personne2.EstMajeur())
#méthode de classe (global pour toutes les personnes)
#Personne.AutreFonction()

#personne1.nom = "toto"
#print("nom1: "+ personne1.nom)
#exercice âge
#estmajeur, mineur
'''
def afficher_informations_personne(nom,age):
    print(f"La personne s'appelle {nom}, son age est {age} ans")
    
nom1= "Jean"
age1=30

afficher_informations_personne(nom1,age1)
'''
#Mises en situation

#code existant



# Personne

#personne.espece_etre_vivant
#---> personne1.espece_etre_vivant (copie variable de classe pour faire variable d'instance)
#self.espece_etre_vivant
#self.espece_etre_vivant



chat= Chat()
chat.AfficherInfosVivant()

EtreVivant= EtreVivant()
EtreVivant.AfficherInfosVivant()

etudiant=Etudiant("Jean",20,"Ecole d'ingénieur informatique")
etudiant.SePresenter()
etudiant.AfficherInfosVivant()
#Héritage

