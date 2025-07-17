from app import app

@app.route('/')
@app.route('/index')
def index():
  return "Hi Iddy. Love you. Bye"