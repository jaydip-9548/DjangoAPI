from rest_framework import serializers
from .models import DepartmentData,EmployeeData

class DepartmentDataSerializer(serializers.Serializer):
     DepartmentName = serializers.CharField(max_length=50)
     
     def create(self, validated_data):
          return DepartmentData.objects.create(**validated_data)
     
     def update(self, instance, validated_data):
        instance.DepartmentName = validated_data.get('DepartmentName',instance.DepartmentName)
        instance.save()
        return instance


class EmployeeDataSerializer(serializers.Serializer):
    EmployeeName = serializers.CharField(max_length=50)
    DepartmentName = serializers.CharField(max_length=50)
    DateOfJoining = serializers.DateField()
    PhotoName = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
         return EmployeeData.objects.create(**validated_data)
    
    
     
    def update(self, instance, validated_data):
        instance.EmployeeName = validated_data.get('EmployeeName',instance.EmployeeName)
        instance.DepartmentName = validated_data.get('DepartmentName',instance.DepartmentName)
        instance.DateOfJoining = validated_data.get('DateOfJoining',instance.DateOfJoining)
        instance.PhotoName = validated_data.get('PhotoName',instance.PhotoName)
        instance.save()
        return instance
    