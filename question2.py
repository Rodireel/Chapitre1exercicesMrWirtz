#Il faut tout mettre en place pour utiliser le SQL
import sqlite3
#utiliser le fichier en db
conn = sqlite3.connect('/Users/rodibaran/Downloads/NoSQL-master/data/Chap1/bc.db')
#donner les commandes pour trouver le résultat
df.to_sql('AZ', conn, if_exists='replace')
#Nous trouvons donc 569 comme réponse à la question 2
