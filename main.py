from flask import Flask, request, render_template
from random import randint

app = Flask(__name__)
cache = {'favorite number': None}

# Landing Page
@app.route('/')
def index():
    return 'Interact with data using /favorite_number or /debug'

# Background Info to Show on Terminal
@app.route('/debug', methods=['GET','POST'])
def debug():
    print(f'My json was {request.json}')
    print(f'My form was {request.form}')
    print(f'My args was {request.args}')
    print(f'My method was {request.method}')
    return ''


# Updates cashe with either GET or POST.
@app.route('/favorite_number', methods=['GET','POST'])
def favorite_number():
    if request.method == 'GET':
        return f'read favorite number {cache}'
    elif request.method == 'POST':
        cache["favorite number"] = randint(1, 100)
        return f'updated favorite number {cache}'


if __name__ == '__main__':
    app.run(debug=True)


'''
Terminal Commands:

$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/favorite_number?foo=bar
$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/favorite_number?foo=bar
$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -X POST http://127.0.0.1:5000/favorite_number?foo=bar
$ curl -d "{\"key1\":\"value1\", \"key2\":\"value2\"}" -X GET http://127.0.0.1:5000/favorite_number?foo=bar

'''

# We'll need this later:     request.args.get('key')
