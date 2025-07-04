from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError  
from market.models import User  
class RegisterForm(FlaskForm):
    
    
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists. Please try a different one.')
        
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email_address=email_to_check.data).first()
        if email:
            raise ValidationError('Email already exists. Please try a different one.')
        
            
    username = StringField(label='Username' , validators=[DataRequired(message='Username is Required'), Length(min=3, max=30)])
    email = StringField(label='Email' , validators=[DataRequired(message='Please Enter Your Email'), Email(message='Invalid Email Address')])
    password1 = PasswordField(label='Password' , validators=[DataRequired(message='Enter Your Password'), Length(min=6, max=25)])
    password2 = PasswordField(label='Confirm Password' , validators=[DataRequired(message='Confirm Your Password'), EqualTo('password1', message='Passwords must match')])
    submit = SubmitField('Create Account')