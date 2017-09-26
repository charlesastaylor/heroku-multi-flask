from flask import Flask

## Configuration



app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask 2"

@app.route("/otherpage")
def otherpage():
    return "Flask 2 Other Page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5002)
