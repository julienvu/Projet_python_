#Paul
#25
#Sophie, Marie, Jean
#Pierre
#18
#Eric,Marc

#Sérialiser DATA - >dumps
#désérialiser - > load

"""
personne = {"nom": "Paul",
            "age":25,
            "amis": ["Sophie", "Marie", "Jean"]            
            
}
personne_json= json.dumps(personne)
print(personne_json)

f=open("fichier_json.txt", "w")
f.write(personne_json)
f.close()

"""


f=open("fichier_json.txt", "r")
donnees_json=f.read()
personne=json.loads(donnees_json)
f.close()