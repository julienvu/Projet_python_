# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions


#Pratiquer sur la POO
#mener raisonnement
#travailler sur du code existant
# question
#titre
# choix str, 
# bonne réponse str
# poser() bool
#questionnaire 
#questions   -Question
#lancer ()
#(données actions à définir)


class Question:
    def __init__(self,titre:str, choix:str, bonne_reponse:str):
        self.titre=titre
        self.choix=choix
        self.bonne_reponse=bonne_reponse
    #méthode statique /de classe
    
    def FromData(data):
        q = Question(data[2], data[0], data[1])
        return q
    
    def poser(self):
        print("Question")
        question=print("   "+self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_response_correcte = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.bonne_reponse.lower():
            print("Bonne réponse")
            resultat_response_correcte = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_response_correcte
        
    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return demander_reponse_numerique_utlisateur(min, max)
    

class Questionnaire:
    def __init__(self,questions):
        self.questions=questions
        
    def lancer(self):
        score = 0
        for question in self.questions:
            if Question.poser(question):
                score += 1
        print("Score final :", score, "sur", len(self.questions))
        return score
    
    
'''
titre = question[0]
choix = question[1]
bonne_reponse = question[2]
'''

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print("Score final :", score, "sur", len(questionnaire))

'''
questionnaire = (
    ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    ("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
                )

lancer_questionnaire(questionnaire)
'''

#data = (("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"))
#q=Question.FromData(data)
#q.poser()


#data = (("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"))
#q=Question.FromData(data)
#approche évoluer le programme plus facilement
#print(q.__dict__)
#question1=Question("Quelle est la capitale de la France ?",("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris")
#question1.poser()

"""
Questionnaire((
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"), 
    Question("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Anvers", "Bruxelles", "Bruges", "Liège"), "Bruxelles")
)).lancer()"""