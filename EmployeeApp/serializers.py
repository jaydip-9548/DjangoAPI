from rest_framework import serializers
from EmployeeApp.models import Departments,Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        field = ('DepartmentId',
                 'DepartmentName')
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        field = ('EmployeeId',
                 'EmployeeName',
                 'Department',
                 'DateOfJoining',
                 'PhotoFileName')