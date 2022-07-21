from app import app
from flask import jsonify, make_response, render_template, request, url_for
from app.routes.decorators import token_required


@app.route('/')
def home():
    return render_template('registrar_sensor.html')

@app.route('/register', methods=['POST'])
def register():
    form_data = request.form
    form_data.get('nome')
    return make_response()
