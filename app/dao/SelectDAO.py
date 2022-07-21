from app.database.querys import query_select_sensor, query_select_tipos_leitura, query_select_tipos_sensor
from app.database.db import cursor

class SelectDAO(object):
    def buscar_tipos_sensores(self):
        cursor.execute(query_select_tipos_sensor())
        return cursor.fetchall()
        
    def buscar_tipos_leituras(self):
        cursor.execute(query_select_tipos_leitura())
        return cursor.fetchall()
    
    def buscar_sensor_nome(self,nome):
        cursor.execute(query_select_sensor(nome))
        return cursor.fetchone()
