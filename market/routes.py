from market import app
from flask import render_template, redirect, url_for, flash
from market.forms import RegisterForm
from market.models import User
from market import db



@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                            email_address=form.email.data,
                            password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('home_page'))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}')
        
    return render_template('register.html', form=form)
