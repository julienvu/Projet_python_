#coding= utf-8 # type: ignore
#récupérer saut de ligne
import os.path


#filename= os.path.join("julien","Projet_Python","mon_fichier.txt")#chemin répertoire
#print("filename:"+ filename)
if os.path.exists("toto"):
    os.rmdir("toto")
f="mon_fichier.txt"
if os.path.exists(f):#fichier existe ou non
    print("Le fichier existe")
    f=open(f,"r")
    texte=f.read()
    print(texte)
    f.close()
else:
    print("Le fichier n'existe pas.")



"""
try:
    f=open("mon_fichiesdfsdr.txt","r")
    
except FileNotFoundError: 
    print("Erreur: le fichier n'a pas pu être ouvert car il n'a pas été trouvé")
else:
    texte=f.read()
    print(texte)
    f.close()
    
    
"""
"""texte=f.readline()
print(texte, end="")
texte=f.readline()
print(texte)
"""

"""
for line in f:
    print(line, end="")
"""



