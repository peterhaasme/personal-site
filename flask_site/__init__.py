# /flask_site/__init__.py
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug=True

@app.route('/')
def index():
    return render_template('index.html')
