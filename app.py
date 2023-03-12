from flask import Flask, render_template, redirect, url_for
from flask import request
from flask import url_for

import forms

from flask import jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.route('/', methods=['GET', 'POST'])
def index():
    frm_alummno = forms.UserForm(request.form)

    if request.method == 'POST':
        alum = Alumnos(nombre = frm_alummno.nombre.data, 
                       apellidos = frm_alummno.apellidos.data, 
                       email = frm_alummno.email.data)

        db.session.add(alum)

        db.session.commit()

        return redirect(url_for('ABCompleto'))

    return render_template('index.html', form = frm_alummno)


@app.route('/ABCompleto', methods=['GET', 'POST'])
def ABCompleto():
    frm_alummno = forms.UserForm(request.form)

    alumnos = Alumnos.query.all()

    return render_template('ABCompleto.html', form = frm_alummno, alumnos = alumnos)


@app.route('/modificar', methods=['GET', 'POST'])
def modificar():

    frm_alummno = forms.UserForm(request.form)

    if request.method == 'GET':

        id = request.args.get('id')
        
        #SELECT * FROM alumnos WHERE id = id
        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        frm_alummno.id.data = alumno.id
        frm_alummno.nombre.data = alumno.nombre
        frm_alummno.apellidos.data = alumno.apellidos
        frm_alummno.email.data = alumno.email

    if request.method == 'POST':
        
        id = frm_alummno.id.data

        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        alumno.nombre = frm_alummno.nombre.data
        alumno.apellidos = frm_alummno.apellidos.data
        alumno.email = frm_alummno.email.data

        db.session.add(alumno)
        db.session.commit()

        return redirect(url_for('ABCompleto'))

    return render_template('modificar.html', form = frm_alummno)

@app.route('/eliminar', methods=['GET'])
def elimnar():
    
    if request.method == 'GET':
        
        id = request.args.get('id')

        alumno = db.session.query(Alumnos).filter(Alumnos.id == id).first()

        db.session.delete(alumno)
        db.session.commit()

        return redirect(url_for('ABCompleto'))

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=5000)


