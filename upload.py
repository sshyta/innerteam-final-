import os
from flask import Flask, render_template, url_for, flash, request, redirect, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import secure_filename
from sqlalchemy import insert
import docx
from main import Init

#
# def new_init(a, b, c, d, e, f, g, h, j, k, l, m, n, o, p, q, r, s, t):
#     print('aa')
#     ins = Init.insert()
#     new_user = ins.values(id=a, name=b, description=c, rating=d, cases=e, benefit=f, organization=g, requ=h, sert=j, FullName=k, post=l, numb=m, mail=n, face=o, INN=p, peoples=q, link=r, where=s, presentation=t)


def new_init(x):
    print(x)
    insert(Init).values(name=[0], description=x[1], rating=x[2], cases=x[3], benefit=x[4], organization=x[5], requ=x[6], sert=x[7], FullName=x[8], post=x[9], numb=x[10], mail=x[11], face=x[12], INN=x[13], peoples=x[14], link=x[15], where=x[16], presentation=x[17])


def oopen(file):
    doc = docx.Document(file)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
        #return new_init(text)
    print(text)




UPLOAD_FOLDER = 'G:/My dok/PY/h3/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'}




app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file', filename=filename)), oopen(file)
    return '''
    <!doctype html>
    <title>Загрузить новый файл</title>
    <h1>Загрузить новый файл</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    </html>
    '''
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


if __name__ == "__main__":
    app.run(debug=True)