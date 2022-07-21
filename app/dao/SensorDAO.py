from app.models.Sensor import Sensor
from app.database.querys import inserir_leitura_has_sensor, query_inserir_sensor
from app.database.db import cursor, conn

class SensorDAO:
	def __init__(self):
		pass

	def salvar(self,sensor: Sensor):
		cursor.execute(query_inserir_sensor(
			nome=sensor.nome,
			senha=sensor.senha,
			chave_privada=sensor.chave_privada,
			chave_publica=sensor.chave_publica,
			id_tipo_leitura=sensor.id_tipo_leitura
		))
		try:
			conn.commit()
		except Exception as e:
			print(e.with_traceback())
