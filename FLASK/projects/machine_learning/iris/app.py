import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template

# create an instance of the Flask class
app = Flask(__name__)

# Load pickle model
model = pickle.load(open('./assets/model.pkl', 'rb'))

# Create Homepage


@app.route('/')
def Home():
    return render_template('index.html')

# API endpoint


@app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template('index.html', prediction_text='The species of the iris flower is {}'.format(prediction))


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
