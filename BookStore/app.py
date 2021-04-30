from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/admin')
def admin():
    return 'welcome admin'

@app.route('/guest/')