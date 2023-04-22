from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='Hello, World!')

@app.route('/greet/<string:name>')
def greet(name):
    return jsonify(message=f'Hello, {name}!')

if __name__ == '__main__':
    app.run(debug=True)
