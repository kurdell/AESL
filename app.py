from flask import Flask, render_template, redirect

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
