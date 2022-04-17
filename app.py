from flask import Flask

app = Flask("abc")

@app.route("/")
def index():
    return "Hello World!"
