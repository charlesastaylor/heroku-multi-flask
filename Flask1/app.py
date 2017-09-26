from flask import Flask, redirect

## Configuration



app = Flask(__name__)

@app.route("/")
def home():
    # return "Welcome to Flask 1"
    return redirect("http://localhost:3000")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
