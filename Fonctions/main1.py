#afficher_table_multiplication(n)
#min/max
#erreur: si min > max => erreur

"""
def afficher_table_multiplication(numero_table):
    min=1
    max=10
    print("Table de multiplication de ",numero_table)
    for i in range(max):
        print(i+1,"*",numero_table," = ",(i+1)*numero_table)
        if(min>max):
            print("Erreur")
            break
        

#afficher_table_multiplication(4)

#correction

def afficher_table_multiplicationcorr(n,min=1,max=10):
    print("Table de multiplication de ",n)
    if min >max:
        print("ERREUR: le min est supérieur au max")
        #utile si en cas d'erreur
        return 
    for i in range(min,max+1):
        print(i,"*",n," = ",(i)*n)
        
        

afficher_table_multiplicationcorr(5,10,1)
"""
"""
def question_1():
    print("Quelle est la capitale de la France ?")
    print("(a) Marseille")
    print("(b) Nice")
    print("(c) Paris")
    print("(d) Nantes")
    print()
    reponse=input("Votre réponse :   ")
    if reponse=="c":
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")
    


def question_2():
    print()
    print("Quelle est la capitale de l'Italie ?")
    print("(a) Rome")
    print("(b) Venise")
    print("(c) Florence")
    print("(d) Pise")
    print()
    reponse=input("Votre réponse :   ")
    if reponse=="a":
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")
"""
#fonction à créer
#poser question(question,r1,r2,r3,r4,choix_bonne_reponse)
'''
titre=question[0]
reponses=question[1]
bonne_reponse=question[2]

'''


def demander_reponse_numerique_utilisateur (min,max):
    reponse_str = input("Votre réponse (entre " + str(min)+ "  et " +str(max)+ ") :")
    try:
        reponse_int= int(reponse_str)
        if min <= reponse_int <= max:
            return reponse_int
        print("ERREUR : Vous devez rentrer un nombre entre", min , "et", max )
    except:
        
        print("ERREUR: Veuillez rentrer uniquement des chiffres")
        
    return demander_reponse_numerique_utilisateur (min,max)
    
    
def poser_question1(question):
    #global score#altérer valeur global exception
    choix= question[1]
    bonne_reponse= question[2]
    
    
    print("Question : ",question[0])
    for i in range(len(choix)):
        print(" ",i+1, "-", choix[i])
        
    print()
    resultat_reponse_correcte=False
    reponse=demander_reponse_numerique_utilisateur(1, len(choix))
    reponse_int = int(reponse)
    
    if choix[reponse_int-1].lower() == bonne_reponse.lower() :
        print("Bonne réponse")
        print()
        resultat_reponse_correcte=True
        
    else:
        print("Mauvaise réponse")
        #print("La bonne réponse est:" , bonne_reponse)
        
    print()
    resultat_reponse_correcte=False
    

#gérer un score
score=0

'''
    questionnaire[]
    question
        titre= "Quelle est la capitale de la France ?"
        reponses = ("Marseille","Nice","Paris","Nantes")
        bonne_reponse= "Paris"

'''
question1= ("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"), "Paris")
#poser_question1("Quelle est la capitale de la France","Marseille","Nice","Paris","Nantes", "c")
#poser_question1("Quelle est la capitale de l'Italie ?","Rome","Venise","Florence","Pise", "a")
question2= ("Quelle est la capitale de l'Italie ?",("Rome","Venise","Florence","Pise"), "Rome")
question3=("Quelle est la capitale de la Belgique ?",("Anvers","Bruxelles","Bruges","Liège"), "Bruxelles")

def lancer_questionnaire(questionnaire):
    score=0
    for question in questionnaire:
        if poser_question1(question):
            poser_question1(question)
            score+=1
    print("Score final: ", score)


'''

poser_question1(question1)
poser_question1(question2)  
poser_question1(question3) 
'''
questionnaire=(
    ("Quelle est la capitale de la France ?",("Marseille","Nice","Paris","Nantes"), "Paris"),
    ("Quelle est la capitale de l'Italie ?",("Rome","Venise","Florence","Pise"), "Rome"), 
    ("Quelle est la capitale de la Belgique ?",("Anvers","Bruxelles","Bruges","Liège"), "Bruxelles")
    
    )
#code meilleure qualité gérer données pas mélanger les données à l'intérieur de l'implémentation archiecture 
#code plus évolutive
lancer_questionnaire(questionnaire)
 




