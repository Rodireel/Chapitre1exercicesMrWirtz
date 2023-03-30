import random
import sqlite3
conn = sqlite3.connect('/Users/rodibaran/Downloads/NoSQL-master/data/Chap1/bc.db')
c = conn.cursor()
#Les conditions
for i in range(50000, 10000001, 2):
 c.execute('INSERT INTO tomatch (id_, rdm_float) VALUES (?, ?)', (i, rdm_float))
conn.commit()
conn.close
