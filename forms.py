from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Correo')


    # username = StringField('Username', [
    #     validators.length(min=4, max=25, message='Username must be between 4 and 25 characters long'),
    #     validators.Required(message='Username is required')
    # ])
    # email = EmailField('Email', [
    #     validators.Required(message='Email is required'),
    #     validators.Email(message='Invalid email')
    # ])
    # age = IntegerField('Age', [
    #     validators.Required(message='Age is required'),
    #     validators.NumberRange(min=18, max=100, message='Age must be between 18 and 100')
    # ])








