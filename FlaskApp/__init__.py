from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hello from Flask in l-flask-sentdex on Apache"


if __name__ == "__main__":
    app.run(host="192.168.1.122")
