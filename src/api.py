# flask starts a service accessible in the browser under
#
#   http://127.0.0.1:5000/
#
# Use here the `route()` decorator to tell Flask what URL should trigger our function
#
#  Here define ressources that are
#
#  http://127.0.0.1:5000/
#  -> hello world
#
#  http://127.0.0.1:5000/hello_world
#  -> HTTP version of hello world
#
#  http://127.0.0.1:5000/training_data
#  -> prints content of training_data in browser
#
#  http://127.0.0.1:5000/predict?zylinder=6&ps=133&gewicht=3410&beschleunigung=15.8&baujahr=71
#  -> predict a price based on the trained model


from flask import Flask, Response, request
import pandas as pd
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # signalisieren von wem Anfragen kommen dürfen

training_data = pd.read_csv(os.path.join('data', 'auto-mpg.csv'))
print(f"DataFrame keys: {training_data.columns}")

trained_model = pd.read_pickle(os.path.join('data', 'models', 'trained_model.sav'))


# Definition of API Ressources


@app.route('/', methods=['GET'])
def main():
    # JSON Response
    return {
        "hello": "world",
    }


@app.route("/hello_world", methods=['GET'])
def hello_world():
    # HTML Response
    return "<p>Hello, World </p>"


@app.route('/training_data', methods=['GET'])
def get_training_data():
    # JSON with defined mimetype
    return Response(training_data.to_json(), mimetype='application/json')


@app.route('/predict', methods=['GET'])
def model_predict():
    # retrieve input from server
    zylinder = request.args.get('zylinder')
    ps = request.args.get('ps')
    gewicht = request.args.get('gewicht')
    beschleunigung = request.args.get('beschleunigung')
    baujahr = request.args.get('baujahr')
    print(f"Request with zylinder={zylinder}, ps={ps}, gewicht={gewicht}, "
          f"beschleuningung={beschleunigung}, baujahr={baujahr}")
    # model prediction for baujahr
    prediction_data = [zylinder, ps, gewicht, beschleunigung, baujahr]
    prediction = trained_model.predict([prediction_data])
    # JSON Response
    return {
        "result": prediction[0]
    }
