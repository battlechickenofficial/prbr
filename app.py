from flask import Flask, redirect, render_template, request, session, send_from_directory
from flask.templating import render_template
from flask.wrappers import Request
import room
import os

import threading
import netManager

app = Flask(__name__)
coms = threading.Thread(target=netManager.run)
coms.start()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        msg = request.form.get("id")
    return render_template("index.html")

@app.route("/draw")
def draw():
    return render_template("draw")


@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0')