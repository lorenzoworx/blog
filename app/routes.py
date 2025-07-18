from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user
import sqlalchemy as sa

@app.route('/')
@app.route('/index')
def index():
  user_profile = {'username': 'Iddy'}
  posts = [
    {
      'author': {'username': 'Oshoke'},
      'body': 'The quick brown fox jumps over the lazy dog'
    },
    {
      'author': {'username': 'Bubu'},
      'body': 'Lorem ipsum sit dolor amet'
    }
  ]
  return render_template('index.html', title='Home', user=user_profile, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  
  form = LoginForm()
  if form.validate_on_submit():
    user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
    if not(User) or not(user.check_password(form.password.data)):
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)