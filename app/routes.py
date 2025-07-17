from flask import render_template
from app import app

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