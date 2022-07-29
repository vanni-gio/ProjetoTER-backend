from app import app
from flask import jsonify, make_response, render_template, request, url_for, redirect
from app.dao.SensorDAO import SensorDAO
from app.dao.SelectDAO import SelectDAO
from app.models.Sensor import Sensor
from criptografia import generate_keys
from werkzeug.security import generate_password_hash

sensorDAO = SensorDAO()
selectDAO = SelectDAO()
@app.route('/')
def home():
    return render_template('registrar_sensor.html',
        tipos_sensor=selectDAO.buscar_tipos_sensores(),
        tipos_leitura=selectDAO.buscar_tipos_leituras()
    )

@app.route('/register', methods=['POST'])
def register():
    form_data = request.form
    pubkey, privkey = generate_keys()
    sensor = Sensor(
        nome=form_data.get('nome'),
        senha=generate_password_hash(form_data.get('senha')),
        topico_mqtt=form_data.get('topico'),
        chave_privada=str(privkey.save_pkcs1()),
        chave_publica=str(pubkey.save_pkcs1()),
        id_tipo_leitura=form_data.get('tipo_leitura')
    )
    sensorDAO.salvar(sensor)
    return redirect(url_for('home'))

@app.route('/sensor', methods=['POST'])
def sensor():
    nome_sensor = request.get_json().get('nome')
    sensor = selectDAO.buscar_sensor_nome(nome_sensor)
    if sensor:
        return jsonify({'id': sensor[0], 'senha': sensor[1]}), 200
    return make_response('Could not find sensor!', 403, {'WWW-Authenticate': 'Basic-realm= "Sensor not registered!"'})

@app.route('/publicert', methods=['POST'])
def certificado_publicod():
    return jsonify({'certificado_mqtt': "ablueblue"}), 200

