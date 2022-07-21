
def inserir_sensor(nome,chave_privada,chave_publica,id_tipo_leitura):
	return f'''
    		INSERT INTO sensor(nome,chave_privada,chave_publica,id_tipo_leitura) VALUES ({nome},{chave_privada},{chave_publica},{id_tipo_leitura});
    	'''

def inserir_leitura_has_sensor(id_tipo_leitura, id_sensor):
	return f'''
		INSERT INTO leitura_has_sensor(id_tipo_leitura, id_sensor) VALUES ({id_tipo_leitura}, {id_sensor});
	'''
