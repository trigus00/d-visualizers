import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
    Display adult population by native country and education
'''

conn = sqlite3.connect('db/adult.db')
cur = conn.cursor()

countries = []
qry = ('SELECT DISTINCT native_country '
      'FROM ADULT '
      'ORDER BY native_country ASC')
cur.execute(qry)
rs = cur.fetchall()
for r in rs:
    countries.append(r[0])
#print(countries)

education = []
qry = ('SELECT DISTINCT education '
      'FROM ADULT '
      'ORDER BY education_num ASC')
cur.execute(qry)
rs = cur.fetchall()
for r in rs:
    education.append(r[0])
#print(education)

dic_e = {}
for e in education:
    dic_c = {}
    for c in countries:
        qry = ('SELECT count(*) counter '
            'FROM ADULT '
            'WHERE education=\'{e}\' '
            'AND native_country=\'{c}\''.format(e=e,c=c))
        cur.execute(qry)
        rs = cur.fetchall()
        for r in rs:
            dic_c[c] = r[0]
    dic_e[e] = dic_c

list_b = []
for k, v in dic_e['Bachelors'].items():
    list_i = []
    list_i.append(k)
    list_i.append(v)
    list_b.append(list_i)

#print(list_b)
df = pd.DataFrame(list_b, columns=['Country', 'Count'])
#print(df)

sns.set(style="whitegrid")
ax = sns.barplot(x="Country", y="Count", data=df)
plt.setp(ax.get_xticklabels(), rotation=60)
plt.show()
