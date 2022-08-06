
def query_inserir_sensor():
	return f'''
    		INSERT INTO sensor(nome,senha,
			topico_mqtt,chave_privada,chave_publica,id_tipo_sensor) VALUES (?,?,?,?,?,?);
    	'''

def inserir_leitura_has_sensor():
	return f'''
		INSERT INTO leitura_has_sensor(id_tipo_leitura, id_sensor) VALUES (?,?);
	'''
def query_select_tipos_sensor():
	return f'''
		SELECT id,tipo FROM tipo_sensor;
	'''

def query_select_tipos_leitura():
	return f'''
		SELECT id,tipo FROM tipo_leitura;
	'''

def query_select_sensor(nome):
	return f'''
		SELECT id, senha FROM sensor WHERE sensor.nome = '{nome}';
	'''

def select_sensores():
	return '''SELECT * FROM sensor;'''