# main.py 

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulation, it's a web app!"