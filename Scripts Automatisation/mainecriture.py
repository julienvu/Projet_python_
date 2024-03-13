#Fichiers texte
#coding=utf-8
#ouvrir (open) <- nom du fichier, mode

f= open("monfichier_1.txt", "r")

# .....
f.write("Bonjour\n")
l= ["Première phrase\n", "Deuxième phrase\n", "Troisième\n"]

f.writelines(l)

f.write("Fin\n")
f.close()



'''
f=open("nombre.txt", "w")


for i in range (10):
    print(i+1)
    f.write(str(i+1)+"\n")
    
f.close()
'''



