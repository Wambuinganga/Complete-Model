from rest_framework import serializers 
from .models import Employee 

class EmployeeSerializers(serializers.ModelSerializer): 
    class meta: 
        model=Employee 
        fields='__all__'