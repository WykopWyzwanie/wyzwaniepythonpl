from flask import Flask, request, session, g, redirect, \
            abort, render_template, flash, url_for, \
            send_from_directory
from flask.ext import assets
from werkzeug.utils import secure_filename

import os, os.path


app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'py'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

# @app.route('/')
# def hello_world():
#     return render_template('index.html', msg='Witaj na stronie WyzwaniePython.pl')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if not os.path.exists('./uploads'):
        os.mkdir('./uploads')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
