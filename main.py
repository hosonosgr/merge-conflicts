from flask import Flask
ap = Flask(__name__)

@ap.route('/')
def hello():
    res = "Hello World!!"
    return res

if __name__ == "__main__":
    ap.run(debug=True)
