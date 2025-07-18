from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

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
  form = LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}, remember_me={}'.format(
      form.username.data, form.remember_me.data
    ))
    return redirect(url_for('index'))
  return render_template('login.html', title='Sign In', form=form)