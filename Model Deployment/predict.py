#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify
import pickle

with open("D:\RGT\Code\Machine Learning\Training\model_C=0.01.bin", 'rb') as f_in:
    (dv, model) = pickle.load(f_in)


app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    X = dv.transform(customer)
    y_pred = float(model.predict_proba(X)[0, 1])
    churn = bool(y_pred > 0.5)
    
    result = {
        'churn probability': y_pred,
        'churn': churn
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
