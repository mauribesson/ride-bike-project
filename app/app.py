from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def admin():
    return render_template("index.html")