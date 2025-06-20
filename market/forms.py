from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
class RegisterForm(FlaskForm):
    username = StringField(label='Username' , validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email' , validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password' , validators=[DataRequired(), Length(min=6, max=25)])
    password2 = PasswordField(label='Confirm Password' , validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Create Account')