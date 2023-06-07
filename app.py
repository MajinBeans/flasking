from flask import Flask
app = Flask(__name__)
images = [
    "https://i.kym-cdn.com/photos/images/original/000/181/190/tumblr_lsdptrZkpi1qh6cr0o4_r1_500.gif"
]
@app.route('/')
def hello():
    return "Me Too."