from bs4 import BeautifulSoup

f=open("recette.html", "r")

html_content= f.read()
f.close()

soup=BeautifulSoup(html_content, "html.parser") #soup:  <! DOCTYPE html>/n 

titre_h1= soup.find("h1") #titre_h1: <h1> Gateau au chocolat </h1>

#list_div_cntre=soup.find_all("div", class_= "centre")#erreur de codage non type has not attribute texte
#catégorie pas description trouver le premier


print(titre_h1.text)
paragraphe_description= soup.find("p", class_= "description")#retourner none pour le résultat affiché avec .text

div_info= soup.find("div", class_="info")
img_info=div_info.find("img")

texte_titre= titre_h1.text

print("Paragraphe de description:", paragraphe_description.text)
print("Titre de la page HTML:", titre_h1.text)
print("Le serc de l'image est:", img_info["src"])

