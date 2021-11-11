# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import example_module as em

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Homepage ja'

@app.route('/hello_user')
def hello_matta():
    A = request.args.get('A')
    B = request.args.get('B')
    text_to_show = f'hello! welcome khun {A} ans khun {B}'
    return text_to_show

