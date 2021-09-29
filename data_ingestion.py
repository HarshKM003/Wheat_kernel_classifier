import sqlite3
import pandas as pd

conn = sqlite3.connect('seeds_new.db')
cols = ['Area','Perimeter','Compactness','Length','Width','Asymmetry Coefficient','Length of kernel Groove','Kernel type']
df = pd.read_csv('Data/seeds_dataset.csv', names=cols, sep='\t')
df.to_sql('Kernel',conn, if_exists='replace',index=False)
cur = conn.cursor()
for row in cur.execute('SELECT * FROM Kernel'):
    print(row)

conn.close()