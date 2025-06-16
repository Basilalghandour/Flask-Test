from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email = StringField(label='Email')
    password1 = StringField(label='Password')
    password2 = StringField(label='Confirm Password')
    submit = SubmitField('Register')