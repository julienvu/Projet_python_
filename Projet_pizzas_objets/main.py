#noms, prix, ingrédients , végétariennes

class Pizza:
    
    def __init__(self, nom, prix, ingredients, vegetarienne=False):
        self.nom = nom
        self.prix= prix
        self.ingredients=ingredients
        self.vegetarienne=vegetarienne
        
    def Afficher(self):
        veg_str= ""
        if self.vegetarienne:
            veg_str= " - VEGETARIENNE"
        print(f"PIZZA {self.nom} : {self.prix} £ "+veg_str)
        print(", ".join(self.ingredients))#sans les parenthèses
        print()
        
#pizza1= Pizza("4 fromages", 8.5 , ("Brie", "emmental", "compté", "parmesan"))
#print(pizza1)#affiche objet mais pas les données
#print(pizza1.nom)
#pizza1.Afficher()

#ingredients=("Brie", "emmental", "compté", "parmesan")


class PizzaPersonnalisee(Pizza):
    PRIX_DE_BASE= 7
    PRIX_PAR_INGREDIENT= 1.2
    dernier_numero=0
    
    def __init__(self, numero):
        PizzaPersonnalisee.dernier_numero+=1
        self.numero=PizzaPersonnalisee.dernier_numero
        #pas d'append avec des tuples mais avec des listes
        super().__init__("Personnnalisée",str(self.numero), [])
        self.demander_ingredients_utilisateur()
        self.calculer_le_prix()
        
        
    def demander_ingredients_utilisateur(self):
        print()
        print(f"Ingrédients pour la pizza personnalisée {self.numero} ")
        while True:
            ingredient=input("Ajoutez un ingrédient (ou ENTER pour terminer) :   ")
            if ingredient =="":
                return
            self.ingredients.append(ingredient)
            print(f"Vous avez {len(self.ingredients)} ingredients(s): {', '.join(self.ingredients)}")
            
    def calculer_le_prix(self):
        self.prix= self.PRIX_DE_BASE+ len(self.ingredients)*self.PRIX_PAR_INGREDIENT
        
    
liste_pizzas=[
    Pizza("4 fromages", 17,("parmesan", "compté"), True), 
    Pizza("Margharita", 14,("parmesan", "mozarella", "lardon","olives", "tomate"), False), 
    Pizza("Oriental", 18.8,("feta", "Merguez"), False),
    PizzaPersonnalisee(1),
    PizzaPersonnalisee(2)
]

def tri(e):
    return len(e.ingredients)

#liste_pizzas.sort(key= tri)

#4 fromages et Végératienne 4 fromages végétarienne

print("Affichage liste des pizzas: ")

# (1) les pizzas végétariennes
#( 2) pizzas non végétariennes
# pizzas qui ont de la tomate
for pizza in liste_pizzas:
    #if not(pizza.vegetarienne):
    #    pizza.Afficher()
    #if "tomate" in pizza.ingredients:
    #    pizza.Afficher()
    #if pizza.prix <10:
    #    pizza.Afficher()
    pizza.Afficher()#pas affichage possible pour les tuples sort tri
    

