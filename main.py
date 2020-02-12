from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)
cashe = {'favorite number': None}


@app.route('/')
def index():
    return 'Interact with data using /read, /update, or /favorite_number'


@app.route('/read')
def read():
    return str(cashe)


@app.route('/update')
def update():
    cashe["favorite number"] = randint(1, 100)
    return str(cashe)


@app.route('/favorite_number', methods=['GET','POST'])
def fav_num():
    print(f'My json was {request.json}')
    print(f'My form was {request.form}')
    print(f'My args was {request.args}')
    print(f'My method was {request.method}')
    return ''


if __name__ == '__main__':
    app.run(debug=True)

# request.args.get('key')
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/favorite_number?foo=bar
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/favorite_number?foo=bar
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -X POST http://127.0.0.1:5000/favorite_number?foo=bar
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -X GET http://127.0.0.1:5000/favorite_number?foo=bar
