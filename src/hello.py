from flask import Flask
app = Flask(__name__)
import os

@app.route("/")
def hello():
    return "Hello Docker-Version2!" + os.environ['PLATFORM']

if __name__ == "__main__":
    app.run(host='0.0.0.0')
