from rest_framework import viewsets 
from rest_framework.decorators import api_view 
from django.core import serializers 
from rest_framework.response import Response 
from rest_framework import status 
from django.http import JsonResponse 
from rest_framework.parsers import JSONParser 
from .models import Employee 
from .serializer import EmployeeSerializers
import pickle
import json
import numpy as np 
from sklearn import preprocessing 
import pandas as pd 
from django.contrib import messages

class EmployeeView(viewsets.ModelViewSet): 
    queryset = Employee.objects.all() 
    serializer_class = EmployeeSerializers


def status(df):
    try:
        scaler=pickle.load(open("/Desktop/Wambui/Employee-Attrition-Predictive-Model/new_df.sav", 'rb'))
        model=pickle.load(open("/Desktop/Wambui/Employee-Attrition-Predictive-Model/trained_model.sav", 'rb'))
        X = scaler.transform(df) 
        y_pred = model.predict(X) 
        y_pred=(y_pred>0.80) 
        result = "Yes" if y_pred else "No"
        return result 
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
