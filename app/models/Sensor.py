class Sensor(object):
    def __init__(self, nome, senha, topico_mqtt, chave_publica,chave_privada, id_tipo_leitura):
        self.nome = nome
        self.senha = senha
        self.topico_mqtt = topico_mqtt
        self.chave_publica = chave_publica
        self.chave_privada = chave_privada
        self.id_tipo_leitura = id_tipo_leitura

    def __get__(self, obj, objtype):                 
        return getattr(obj, self.attr)

    def __set__(self, obj, value):                   
        setattr(obj, self.attr, value) 