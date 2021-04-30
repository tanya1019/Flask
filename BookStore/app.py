from flask import Flask, redirect, url_for,request, render_template

app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'welcome admin'

@app.route('/guest/<username>')
def guest(username):
    return 'welcome %s' % username

@app.route('/profile/<guest>')
def add(guest):
    if guest == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', username = guest))

@app.route('/abc')
def abc():
    return 'this is request page %s' % request.headers

@app.route('/')
def index():
    return render_template('index.html')

















app.run(debug = True)