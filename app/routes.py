from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user_profile = {'username': 'Iddy'}
  return render_template('index.html', title='Home', user=user_profile)