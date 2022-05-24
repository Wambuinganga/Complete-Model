from ast import mod
from turtle import mode
from django.db import models

# Create your models here.

class Employee(models.Model):
    satisfaction_level = models.FloatField(max_length= 100)
    last_evaluation_rating = models.FloatField(max_length= 100)
    projects_worked_on = models.IntegerField()
    average_montly_hours = models.IntegerField()
    time_spend_company  = models.IntegerField()
    work_accident = models.IntegerField()
    promotion_last_5years = models.IntegerField()
    department = models.CharField(max_length=300)
    salary  = models.CharField(max_length= 100)
    attrition = models.IntegerField()


