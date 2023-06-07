from flask import Flask
app = Flask(__name__)
images = [
    "http://knowyourmeme.com/photos/181190-i-like-turtles"
]
@app.route('/')
def hello():
    return "Me Too."