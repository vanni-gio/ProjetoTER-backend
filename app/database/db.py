import sqlite3
import os.path as ospath
import psycopg2 as psql

BASE_DIR = ospath.dirname(ospath.abspath(__file__))
db_path = ospath.join(BASE_DIR, 'projetoTER.db')
conn_sqlite = sqlite3.connect(db_path, check_same_thread=False)
try:
    conn_psql = psql.connect(
        host='ec2-52-205-61-230.compute-1.amazonaws.com',
        database='d6j3vgaift8ile',
        user='zqiusuicrcxeqj',
        password='de6e180d4624309bf13df7595a769267cf6289da3441a54c9f08531dadf12dd2',
        port=5432
    )
except Exception as e:
    print(e)
    exit(0)
