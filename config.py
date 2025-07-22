import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-aint-none-of-your-business'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
  # MAIL_SERVER = os.environ.get('MAIL_SERVER')
  # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 2)
  # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
  # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  ADMINS = ['asocialinfroverf@gmail.com']
  POSTS_PER_PAGE = 20
  MAIL_SERVER = 'localhost'
  MAIL_PORT = 8025
  MAIL_USERNAME = None
  MAIL_PASSWORD = None
  MAIL_USE_TLS = False
  MAIL_USE_SSL = False