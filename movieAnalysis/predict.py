import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'rf_model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('movieRating')

@app.route('/predict', methods=['POST'])
def predict():
    movie = request.get_json()

    X = dv.transform([movie])
    y_pred = model.predict(X)

    result = {
        'movie_rating': float(y_pred)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)