from flask import Flask, url_for

app = Flask(__name__)

from flask import render_template


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/dashboard')
def dash():
    return render_template('index.html')