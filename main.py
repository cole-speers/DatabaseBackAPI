from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)
cache = {'favorite number': None}


@app.route('/')
def index():
    return 'Interact with data using /read, /update, or /favorite_number'


@app.route('/read')
def read():
    return 'read' + str(cache)


@app.route('/update')
def update():
    cache["favorite number"] = randint(1, 100)
    return 'update' + str(cache)


@app.route('/favorite_number', methods=['GET','POST'])
def fav_num():
    print(f'My json was {request.json}')
    print(f'My form was {request.form}')
    print(f'My args was {request.args}')
    print(f'My method was {request.method}')
    return ''


# Creating new route that updates cashe with either GET or POST.
@app.route('/activate', methods=['GET','POST'])
def activate():
    if request.method == 'GET':
        return read()
    elif request.method == 'POST':
        return update()

if __name__ == '__main__':
    app.run(debug=True)

# request.args.get('key')
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/favorite_number?foo=bar
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/favorite_number?foo=bar
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -X POST http://127.0.0.1:5000/favorite_number?foo=bar
#$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -X GET http://127.0.0.1:5000/favorite_number?foo=bar
