from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def admin():
    return render_template("index.jinja")