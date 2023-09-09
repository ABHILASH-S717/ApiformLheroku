# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:13:12 2023

@author: Administrator
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle 
import json

app = FastAPI()


orgins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_orgins = orgins,
    allow_credetials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
    
# loaing the saved model 
diabetes_model = pickle.load(open('diabetes_model(1).sav','rb'))


#there are 2 methods for creating  api 
'''they  are @app.get
@app.post'''

@app.post('/diabetes_predictio')


def dia_pred(input_parameters:model_input):
    
    input_data = input_parameters.json()
    
    # convert it  into dictionary
    input_dictionary = json.loads(input_data)
    
    # convert  into tuple or list
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dbf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    input_list  = [preg,glu,bp,skin,insulin,bmi,dbf,age]
    
    prediction = diabetes_model.predict([input_list])
    
    
    if prediction[0]==0:
        return 'The person is non diabetic'
    
    else:
        return 'The person is diabetic'
    
    