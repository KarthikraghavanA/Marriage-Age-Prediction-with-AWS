import flask
from flask import request
import pickle
from flask_cors import CORS

app = flask.Flask('__name__')
app.config["DEBUG"] = True
CORS(app)

@app.route('/')
def homepage():
    return "<h1>Hello, This is for testing our API</h1>"

@app.route('/predict')
def predict():
    model = pickle.load(open('rfrmodel.pkl', 'rb'))
    age = model.predict([[int(request.args['gender']),
                          int(request.args['religion']),
                          int(request.args['caste']),
                          int(request.args['mother_tongue']),
                          int(request.args['country']),
                          int(request.args['height_cms'])]])
    return str(age)

if __name__ == '__main__':
    app.run(debug=True)