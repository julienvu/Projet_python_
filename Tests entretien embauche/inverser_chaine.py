#inverser chaine

# "bonjour toto"
# "otot ruojnob"
#boucle méthode 1
#slice méthode 2
def reverse_string(str):
    #
    #return chaine_inversee
    chaine_inversee=""
    for c in str:
        #concaténation par la gauche c à gauche
        chaine_inversee = c+chaine_inversee
        #B
        #oB
        #noB
    return chaine_inversee

def reverse_string2(str):
    return s[::-1]  
    
s="Bonjour toto"
#print(reverse_string(s))
# méthode 2: slice
#print(reverse_string2(s))#1 seule instruction donc plus rapide que la méthode avec boucle
# début à la fin en partant de la fin 



