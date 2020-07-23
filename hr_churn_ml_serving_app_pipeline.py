import pandas as pd
import numpy as np 
import pickle
import sys
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/employee_churn', methods = ['POST']) 
def serve_employee_churn():
    
    predict_data = request.data.decode()
    
    predict_data = predict_data.split(',')
    print(request.data)
    explain_data = []
    for val in predict_data:
        if val.replace('.', '', 1).replace('"','',1).isdigit() == True:
            explain_data.append(float(val))
        else:
            explain_data.append(str(val))
    print(type(explain_data))
    print(explain_data)
    data = pd.DataFrame([explain_data] , columns = ['satisfaction_level', 'last_evaluation', 'number_project','average_montly_hours', 'time_spend_company', 'Work_accident','promotion_last_5years', 'Department', 'salary'])
    for feature in data:
        if data[feature].dtype == 'object' or data[feature].dtype == 'bool':
            file = open(feature+'_le.pkl','rb')
            le = pickle.load(file)
            file.close()
            data[feature] =le.transform(data[feature])
            
    file = open('HR_Churn_Model.pkl','rb')
    model = pickle.load(file)
    file.close()
    
    try:
        model_predict = model.predict(np.array(data.loc[0,:]).reshape(1,-1))
        print(model_predict[0])
        return jsonify(str(model_predict[0]))
    except Exception as e:
        print(e)
        return jsonify(e)
    
if __name__ == '__main__':
    app.run( port = 5001 )
    