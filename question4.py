import random
import sqlite3
conn = sqlite3.connect('/Users/rodibaran/Downloads/NoSQL-master/data/Chap1/bc.db')
#Les conditions
conditions=[(i, random.random()) for i in range (50000, 10000001, 2)]
c-conn.cursor()
c.executemany('INSERT INTO tomatch (id_, rdm_float) VALUES (?,?)', conditions)
conn.commit()
