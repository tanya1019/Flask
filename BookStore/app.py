from flask import Flask, redirect, url_for, request, render_template, redirect
# pip install sqlalchemy flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(
    os.path.join(project_dir, 'mydatabase.db'))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)


class Book(db.Model):
    name = db.Column(db.String(100), unique=True,
                     primary_key=True, nullable=False)
    author = db.Column(db.String(100), nullable=False)


@app.route('/index')
def index():
    return render_template('index.html')


@app.route("/profile/<username>")
def profile(username):
    return render_template('profile.html', username=username, isActive=False)


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('book.html', books=books)


@app.route('/updatebooks')
def updatebooks():
    books = Book.query.all()
    return render_template('updatebook.html', books=books)

@app.route('/delete', methods = ['POST'])
def delete():
    name = request.form['name']
    book = Book.query.filter_by(name = name).first()
    db.session.delete(book)
    db.session.commit()
    return redirect('/books')


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')
    

@app.route('/submitform', methods=['POST'])
def submitform():
    name = request.form['name']
    author = request.form['author']
    book = Book(name=name, author=author)
    db.session.add(book)
    db.session.commit()
    return redirect('/books')


if __name__ == '__main__':
    app.run(debug=True)
