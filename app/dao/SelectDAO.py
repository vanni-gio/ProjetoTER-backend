from app.database.querys import query_select_sensor, query_select_tipos_leitura, query_select_tipos_sensor
from app.database.db import conn_sqlite, conn_psql
import rsa
import ast

class SelectDAO(object):
    def __init__(self):
        self.cursor_sqlite  = conn_sqlite.cursor()
        self.cursor_psql = conn_psql.cursor()
    def buscar_tipos_sensores(self):
        self.cursor_sqlite.execute(query_select_tipos_sensor())
        return self.cursor_sqlite.fetchall()
        
    def buscar_tipos_leituras(self):
        self.cursor_sqlite.execute(query_select_tipos_leitura())
        return self.cursor_sqlite.fetchall()
    
    def buscar_sensor_nome(self,nome):
        self.cursor_sqlite.execute(query_select_sensor(nome))
        return self.cursor_sqlite.fetchone()

    def buscar_dados(self):
        self.cursor_psql.execute('''
        SELECT 
            id_from_fog
        FROM 
            sensor
        WHERE 
            sensor.idsensor IN (  SELECT DISTINCT
                            idsensor
                        FROM
                            dado
                    );
        ''')
        ids_sensor_psql = self.cursor_psql.fetchall()
        self.cursor_sqlite.execute('SELECT id, chave_privada FROM sensor;')
        ids_sensor_sqlite = self.cursor_sqlite.fetchall()
        s = set(ids_sensor_psql)
        ids = [(id, rsa.PrivateKey.load_pkcs1(chave_privada)) for id, chave_privada in ids_sensor_sqlite if id not in s] # seleciona somente os sensores que possuem dados em cloud
        dados = []
        for id, pk in ids:
            self.cursor_psql.execute(f'''
                    SELECT 
                        dado,tipodado,tipoleitura
                    FROM 
                        dado
                    WHERE 
                        dado.idsensor IN (SELECT 
                                                idsensor
                                            FROM
                                                sensor
                                            WHERE
                                                sensor.id_from_fog = {id}
                                        );
            ''')
            dados.append([{"dado": ast.literal_eval(rsa.decrypt(bytes(dado), pk).decode()), "tipodado": tipodado, "tipoleitura": tipoleitura, "idsensor": id} for dado, tipodado, tipoleitura in self.cursor_psql.fetchall()])
        
        dados.remove([])

        return dados


        
