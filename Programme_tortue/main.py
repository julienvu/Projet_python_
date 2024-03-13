#création module tortue

import turtle

#escalier(taille, nb)
def escalier(taille,nb):
    #section 48 déplacer la tortue
    """
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.backward(100)
    """

    #5 marches de 30 pixels
    #fonction paramètre taille
    for i in range(0,nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        #taille des marches plus petites 
        taille-=10
    
    t.forward(taille)
    
    



def carree(taille):
    
    #section 48 déplacer la tortue
    """
    t.forward(100)
    t.left(90)
    t.forward(50)
    t.backward(100)
    """
    #fonction paramètre taille
    for i in range(0,4):
        t.forward(taille)
        t.left(90)
    
def carres(taille_depart,nb):
    #taille=(i+1) *taille_depart
    for i in range(0,nb):
        taille= (i+1)*(i+1)*taille_depart
        carree(taille)
    
    

t=turtle.Turtle()

#test fonction escalier
#escalier(60,7)
#test carree(50)
#carree(50)
#test carres
#carres(10,10)



#activer la fenêtre
#turtle.done()









