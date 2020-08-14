from flask import Flask, render_template
from flask import request
app = Flask(__name__)

@app.route('/') #http://127.0.0.1:5000/
def index():
    return render_template('index.html')

@app.route('/hello')#http://127.0.0.1:5000/hello?name=A
def hello():
    name = request.args.get('name', '')
    gender = request.args.get('gender')
    salutation = ''
    if gender == 'M': salutation = 'Mr'
    if gender == 'F': salutation = 'Ms'
    return f'Hello {salutation} {name}'

@app.route('/hello2', methods=['POST'])
def hello2():
    name = request.form.get('name', '')
    gender = request.form.get('gender')
    salutation = ''
    if gender == 'M': salutation = 'Mr'
    if gender == 'F': salutation = 'Ms'
    return f'Hello {salutation} {name}'


app.run(debug=True)