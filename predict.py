# from waitress import serve
import pickle

from flask import Flask
from flask import request
from flask import jsonify

model = 'model1.bin'

with open(model, 'rb') as f_in:
    model = pickle.load(f_in)

dict_vect = 'dv.bin'

with open(dict_vect, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    X = dv.transform([client])
    y_pred = model.predict_proba(X)[0, 1]

    result = {
        'churn_probability': float(y_pred)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
