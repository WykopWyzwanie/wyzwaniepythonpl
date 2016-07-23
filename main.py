from flask import Flask, request, session, g, redirect, \
            abort, render_template, flash, url_for
from flask.ext import assets
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'py'}


app = Flask(__name__)

env = assets.Environment(app)

env.load_path = [
        os.path.join(os.path.dirname(__file__),
            'bower_components'),
        ]

env.register(
        'js_all',
        assets.Bundle(
            'jquery/dist/jquery.min.js',
            'bootstrap/dist/js/bootstrap.min.js',
            output='js_all.js'
            )
        )

env.register(
        'css_all',
        assets.Bundle(
            'bootstrap/dist/css/bootstrap.min.css',
            output='css_all.css'
            )
        )

@app.route('/')
def hello_world():
    return render_template('index.html', msg='Witaj na stronie WyzwaniePython.pl')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')
