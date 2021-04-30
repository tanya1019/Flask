from flask import Flask, redirect, url_for

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

app.run(debug = True)