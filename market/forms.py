from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
class RegisterForm(FlaskForm):
    username = StringField(label='Username' , validators=[DataRequired(message='Username is Required'), Length(min=3, max=30)])
    email = StringField(label='Email' , validators=[DataRequired(message='Please Enter Your Email'), Email(message='Invalid Email Address')])
    password1 = PasswordField(label='Password' , validators=[DataRequired(message='Enter Your Password'), Length(min=6, max=25)])
    password2 = PasswordField(label='Confirm Password' , validators=[DataRequired(message='Confirm Your Password'), EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('Create Account')