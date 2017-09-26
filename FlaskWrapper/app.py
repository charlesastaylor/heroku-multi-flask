from flask import Flask
from urllib import request

## Configuration



app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Flask Wrapper"

@app.route("/test/<int:i>")
def test(i):
		return str(i)

@app.route("/flask1/")
@app.route("/flask1/<path:path>")
def flask1(path=""):
	return request.urlopen("https://127.0.0.1:5001/" + path).read()

@app.route("/flask2/")
@app.route("/flask2/<path:path>")
def flask2(path=""):
	return request.urlopen("https://127.0.0.1:5002/" + path).read()

# @app.route("/flask2")
# def test():
#     return request.urlopen("http://localhost:5000").read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
