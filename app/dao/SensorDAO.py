from app.models.Sensor import Sensor
from app.database.querys import inserir_leitura_has_sensor, query_inserir_sensor
from app.database.db import cursor, conn

class SensorDAO:
	def __init__(self):
		pass

	def salvar(self,sensor: Sensor, id_tipo_leitura):
		cursor.execute(query_inserir_sensor(), 
			(sensor.nome,
			sensor.senha,
			sensor.topico_mqtt,
			sensor.chave_privada,
			sensor.chave_publica,
			sensor.id_tipo_sensor)
		)
		id_sensor = cursor.lastrowid
		cursor.execute('INSERT INTO leitura_has_sensor(id_tipo_leitura,id_sensor) VALUES (?,?)', (id_tipo_leitura, id_sensor))
		try:
			conn.commit()
		except Exception as e:
			conn.rollback()
			print(e.with_traceback())
