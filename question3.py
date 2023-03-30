#Il faut dès à présent ajouter des valeurs à la base de données
import csv
import sqlite3
#On retrace le chemin d'accès
conn=sqlite3.connect('/Users/rodibaran/Downloads/NoSQL-master/data/Chap1/bc.db')
c=conn.cursor()
#On met en place les nouveaux éléments de la base de données
c.execute('''CREATE TABLE tomatch (id_ INTEGER PRIMARY KEY, rdm_float)''')
conn.commit
conn.close
