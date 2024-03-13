#SQLITE création table
import sqlite3

con=sqlite3.connect("albums2.db")
curseur=connexion.cursor()

curseur.execute("""CREATE TABLE artiste  (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR);""")