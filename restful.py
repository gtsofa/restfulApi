# restful.py

# import objects from the flask model
from flask import Flask, jsonify, request 

# define an app using flask
app = Flask(__name__)

languages = [{'name':'Python'}, {'name':'Ruby'}, {'name':'JavaScript'}]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message':'It works!'})

@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})


if __name__ == '__main__':
    app.run(debug=True)