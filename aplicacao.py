from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/jogosdarodada')
def jogosdarodada():
    return render_template('jogosdarodada.html')

@app.route('/times')
def times():
    return render_template('times.html')

app.run(debug=True)