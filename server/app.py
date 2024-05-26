from flask import Flask, request, json
import numpy as np
import util

app = Flask(__name__)


@app.route('/get-locations', methods=['GET'])
def get_locations():
    return util._locations


@app.route('/get-types', methods=['GET'])
def get_types():
    return util._types


@app.route('/predict', methods=['POST'])
def predict():
    x = np.zeros(len(util._columns))
    x[0] = request.form.get('area')
    x[1] = request.form.get('furnishing')
    x[2] = request.form.get('bhk')
    location = 'location_'+request.form.get('location')
    x[util._columns.index(location)] = 1
    type_ = 'type_'+request.form.get('type')
    x[util._columns.index(type_)] = 1
    y = util._model.predict([x])
    return {"price" : float(y[0])}


if __name__ == "__main__":
    util.load_resources()
    app.run()
