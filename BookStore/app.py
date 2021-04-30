from flask import Flask, redirect, url_for,request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username = username)

app.run(debug = True)