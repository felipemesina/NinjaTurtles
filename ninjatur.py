from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ninja")
def ninjaMain():
    return render_template("ninjahere.html")

@app.route("/ninja/<color>")
def ninjateam(color=None):
    return render_template("pickaninja.html", color=color)



app.run(debug=True)
