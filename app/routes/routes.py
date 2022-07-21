from app import app
from flask import jsonify, make_response, render_template, request, url_for
from app.routes.decorators import token_required
from backend.app.dao.SensorDAO import SensorDAO
from backend.app.dao.SelectDAO import SelectDAO
from backend.app.models.Sensor import Sensor
from backend.criptografia import generate_keys
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
        topico_mqtt=form_data.get('topico_mqtt'),
        chave_privada=privkey,
        chave_publica=pubkey,
        id_tipo_leitura=form_data.get('id_tipo_leitura')
    )
    sensorDAO.salvar(sensor)
    return make_response()

@app.route('/sensor', methods=['POST'])
def sensor():
    nome_sensor = request.json()['nome']
    sensor, = selectDAO.buscar_sensor_nome(nome_sensor)
    if sensor:
        return jsonify({'id': sensor[0], 'senha': sensor[1]}), 200
    return make_response('Could not find sensor!', 403, {'WWW-Authenticate': 'Basic-realm= "Sensor not registered!"'})

@app.route('/opensslertificate')
def certificados():
    pass