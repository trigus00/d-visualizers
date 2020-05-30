import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

#qry = 'PRAGMA table_info(ADULT)'
#cur.execute(qry)
#rs = cur.fetchall()
#print(rs)

#qry = 'SELECT * FROM ADULT'
#cur.execute(qry)
#rs = cur.fetchall()
#for r in rs:
#    print(r)

qry = ('SELECT sex, count(*) counter '
       'FROM ADULT '
       'GROUP BY sex')
cur.execute(qry)
rs = cur.fetchall()
for r in rs:
    print(r)

df = pd.DataFrame.from_records(rs, columns=['sex', 'counter'])

plt.pie(df['counter'], labels=df['sex'], autopct='%1.1f%%', shadow=False)
plt.title('Sex Pie Chart')
plt.axis('equal')
plt.show()