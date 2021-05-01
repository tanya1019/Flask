from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/profile/<username>")
def profile(username):
    return render_template('profile.html', username=username, isActive=False)


@app.route('/books')
def books():
    books = ['book1', 'book2', 'book3']
    return render_template('book.html', books=books)


app.run(debug=True)
