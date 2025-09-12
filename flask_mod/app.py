from flask import Flask,render_template,request
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route('/')
def index():
  return render_template('login.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/perform_reg' , methods = ['post'])
def perform_reg():
  name = request.form.get('user')
  email = request.form.get('email')
  password = request.form.get('pass')

  response = dbo.insert(name,email,password)

  if response :
    return "registration successful"
  
  else :
    return "email already exist"

app.run(debug=True)