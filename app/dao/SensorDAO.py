from app.models.Sensor import Sensor
from app.database.querys import inserir_leitura_has_sensor, query_inserir_sensor
from app.database.db import cursor, conn

class SensorDAO:
	def __init__(self):
		pass

	def salvar(self,sensor: Sensor):
		print((sensor.nome,
			sensor.senha,
			sensor.topico_mqtt,
			sensor.chave_privada,
			sensor.chave_publica,
			sensor.id_tipo_leitura))
		cursor.execute(query_inserir_sensor(), 
			(sensor.nome,
			sensor.senha,
			sensor.topico_mqtt,
			sensor.chave_privada,
			sensor.chave_publica,
			sensor.id_tipo_leitura)
		)
		try:
			conn.commit()
		except Exception as e:
			print(e.with_traceback())
