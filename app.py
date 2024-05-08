from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Welcome to jenkins</h1>"

if __name__ == "__main__":
    app.run(port=8000, host="0.0.0.0", debug=True )