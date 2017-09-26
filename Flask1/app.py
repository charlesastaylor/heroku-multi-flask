from flask import Flask

## Configuration



app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask 1"

@app.route("/otherpage")
def otherpage():
    return "Flask 1 Other Page"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
