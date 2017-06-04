import os
from flask import Flask, render_template, request, flash,redirect, url_for
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath
from adapt import  apply_threshold
from segall import identify



app = Flask(__name__)

UPLOAD_FOLDER = join(dirname(realpath(__file__)),'templates/images')
ALLOWED_EXTENSIONS = set(['png', 'jpg'])


@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        print("Hello")

        if 'file' not in request.files:
            print("No file")
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            print("No selected file")
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER']))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(filename + " is saved and done !!")
            apply_threshold(filename)
            dig_string = identify()
            print(dig_string)
            return render_template('home.html')

    return  render_template('home.html')









@app.route('/about')
def about():
    return render_template('about.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)

