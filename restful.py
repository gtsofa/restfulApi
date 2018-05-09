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

@app.route('/lang/<string:name>', methods=['GET'])
def returnOne(name):
    #use lamba to search through the list
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})

# Perform POST REQUEST NOW.
@app.route('/lang', methods=['POST'])
def addOne():
    # create a dic key will have json object and whatever value needs to be passed
    language = {'name': request.json['name']}
    print(language)
    languages.append(language)

    return jsonify({'languages': languages})



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True) # c9