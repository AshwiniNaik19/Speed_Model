from django.shortcuts import render
import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn import metrics
# from sklearn.preprocessing import LabelEncoder
from django.shortcuts import render
# from yaml import load
# encoder = LabelEncoder()
import joblib
# from rest_framework.views import APIView
# from rest_framework.response import Response



def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    model = joblib.load("/home/mglocadmin/Desktop/Prediction_in_HTMl_form/Prediction_in_HTMl_form/predict1/Speedmodel_testdata.joblib")

    # li = []
    # li.append(request.GET['n1'])
    # li.append(request.GET['n2'])
    # li.append(request.GET['n3'])
    # li.append(request.GET['n4'])
    var1 = request.GET['n1']
    if var1 == "Fishing":
        var1= 1
    elif var1 == "Military":
        var1= 2
    elif var1 == "Other":
        var1= 3
    elif var1 == "Passenger":
        var1= 4
    elif var1 == "Cargo":
        var1= 5
    elif var1 == "Pleasure Craft" or var1 =="Sailing":
        var1= 6
    elif var1 == "Tanker":
        var1= 7
    elif var1 == "Tug Tow":
        var1= 8
    else:
        var1= "0"
    var2 = request.GET['n2']
    var3 = request.GET['n3']
    var4 = request.GET['n4']
    # pred = model.predict([li])
    # pred = model.predict([var1,var2,var3,var4])
    # pred = round(pred[0])
    pred = model.predict(np.array([var1, var2, var3, var4]).reshape(1, -1))
    pred = round(pred[0])
    
    average_speed = "The Predicted Weighted Average Speed is " + str(pred)

    return render(request, 'output.html', {"result": average_speed, "t1": var1, "t2":var2, "t3":var3, "t4":var4})