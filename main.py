from flask import Flask, render_template, send_from_directory, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/innertea'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Init(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    cases = db.Column(db.String, nullable=False)
    benefit = db.Column(db.String, nullable=False)
    organization = db.Column(db.String, nullable=False)
    requ = db.Column(db.String, nullable=False)
    sert = db.Column(db.String, nullable=False)
    FullName = db.Column(db.String, nullable=False)
    post = db.Column(db.String, nullable=False)
    numb = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, nullable=False)
    face = db.Column(db.String, nullable=False)
    INN = db.Column(db.String, nullable=False)
    peoples = db.Column(db.Integer, nullable=False)
    link = db.Column(db.String, nullable=False)
    where = db.Column(db.String, nullable=False)
    presentation = db.Column(db.String, nullable=False)


class files (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    path = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/bob')
def file():
    return render_template('uppload.html')



@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route("/post/<int:id_post>")
def showPost(id_post):
    db = Init()
    dbase = open(db)
    title, post = dbase.getPost(id_post)
    return render_template('post.html', menu=dbase.getMenu(), title=title, post=post)



@app.route('/')
def Main():
    return render_template('MainPage.html')


@app.route('/Search')
def search():
    return render_template('Search.html')


@app.route('/SearchRes')
def res():
    return render_template('Search_result.html')


@app.route('/AfterSearch')
def MainPage():
    return render_template('MainAfterSearch.html')


if __name__ == "__main__":
    app.run(debug=True)

