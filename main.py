from flask import Flask, render_template
from random import randint

app = Flask(__name__)
cashe = {'favorite number': None}


@app.route('/')
def index():
    return 'Interact with data using /read and /update'

@app.route('/read')
def read():
    return str(cashe)

@app.route('/update')
def update():
    cashe["favorite number"] = randint(1, 100)
    return str(cashe)


if __name__ == '__main__':
    app.run(debug=True)