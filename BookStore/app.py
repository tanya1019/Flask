from flask import Flask, redirect, url_for, request, render_template
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


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/profile/<username>")
def profile(username):
    return render_template('profile.html', username=username, isActive=False)


@app.route('/books')
def books():
    books = [
        {'name': "Book1", 'author': 'Author1', 'cover': 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1594616847'},
        {'name': "Book2", 'author': 'Author2', 'cover': 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1594616847'},
        {'name': "Book3", 'author': 'Author3', 'cover': 'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1594616847'}
    ]
    return render_template('book.html', books=books)


@app.route('/addbook')
def addbook():
    return render_template('addbook.html')


@app.route('/submitform', methods=['POST'])
def submitform():
    name = request.form['name']
    author = request.form['author']
    return 'Book name is %s and Author is %s' % (name, author)


if __name__ == '__main__':
    app.run(debug=True)
