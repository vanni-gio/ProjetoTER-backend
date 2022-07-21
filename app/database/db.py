import sqlite3
import os.path as ospath

BASE_DIR = ospath.dirname(ospath.abspath(__file__))
db_path = ospath.join(BASE_DIR, 'projetoTER.db')
conn = sqlite3.connect(db_path, check_same_thread=False)
print(conn)
cursor = conn.cursor()
