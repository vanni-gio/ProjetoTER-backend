
def inserir_sensor(mqttTopic, nomeSensor, chave, idTipoSensor):
    return f'''
    INSERT INTO Sensor(mqttTopic, nomeSensor, chave, idTipoSensor) VALUES ({mqttTopic}, {nomeSensor}, {chave}, {idTipoSensor});
    '''