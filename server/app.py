from flask import Flask, request,jsonify
import numpy as np
import util

app = Flask(__name__)


@app.route('/get-locations', methods=['GET'])
def get_locations():
    response = jsonify({'locations':util._locations})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict', methods=['POST'])
def predict():
    x = np.zeros(len(util._columns))
    x[0] = request.form.get('area')
    x[1] = request.form.get('furnishing')
    x[2] = request.form.get('bhk')
    location = 'location_'+request.form.get('location').lower()
    x[util._columns.index(location)] = 1
    type_ = 'type_'+request.form.get('type').lower()
    x[util._columns.index(type_)] = 1
    y = util._model.predict([x])
    response = jsonify({"price" : round(float(y[0]),2)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    util.load_resources()
    app.run()
