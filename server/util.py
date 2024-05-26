import pickle
import json

_model = None
_columns = []
_locations = []
_types = []


def load_resources():
    global _model
    global _locations
    global _columns
    global _types

    with open('../model/columns.json','r') as f:
        _columns = json.load(f)['columns']
    _locations = [col[9:] for col in _columns[3:-3]]
    _types = [col[5:] for col in _columns[-3:]]

    with open('../model/model.pickle','rb') as f:
        _model = pickle.load(f)


if __name__ == '__main__':
    load_resources()
    print(_columns)
    print(_locations)
    print(_types)
    print(_model)
