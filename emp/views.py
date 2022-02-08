from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import DepartmentData,EmployeeData
from .serializers import DepartmentDataSerializer,EmployeeDataSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt

def department_detail(request):
    if request.method == 'GET':
        departmentdata = DepartmentData.objects.all()
        serializer = DepartmentDataSerializer(departmentdata,many=True)
        json_data =JSONRenderer().render(serializer.data)
        print("data : ",json_data)
        return HttpResponse(json_data,content_type='application/json')
    
    elif request.method == 'POST':
        py_data = JSONParser().parse(request)
        serializer = DepartmentDataSerializer(data= py_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Data Inserted Success !!")
        return HttpResponse("Data Insertion Failed !!")
    
    elif request.method == 'PUT':
        py_data = JSONParser().parse(request)
        id = py_data.get('id')
        data = DepartmentData.objects.get(id = id)
        serializer = DepartmentDataSerializer(data,data = py_data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Updated Successfully")
        return HttpResponse("Updation Failed")
    
    elif request.method == 'DELETE':
        py_data = JSONParser().parse(request)        
        id = py_data.get('id')
        data = DepartmentData.objects.get(id = id)
        data.delete()
        return HttpResponse("Data deleted succeess !!")
        
        
@csrf_exempt  
def employee_detail(request):
    if request.method == 'GET':
        departmentdata = EmployeeData.objects.all()
        serializer = EmployeeDataSerializer(departmentdata,many=True)
        json_data =JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    
    elif request.method == 'POST':
        py_data = JSONParser().parse(request)
        serializer = EmployeeDataSerializer(data= py_data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Data Inserted Success !!")
        return HttpResponse("Data Insertion Failed !!")
    
    elif request.method == 'PUT':
        py_data = JSONParser().parse(request)
        id = py_data.get('id')
        data = EmployeeData.objects.get(id = id)
        serializer = EmployeeDataSerializer(data,data = py_data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("Updated Successfully")
        return HttpResponse("Updation Failed")
    
    elif request.method == 'DELETE':
        py_data = JSONParser().parse(request)        
        id = py_data.get('id')
        data = EmployeeData.objects.get(id = id)
        data.delete()
        return HttpResponse("Data deleted succeess !!")
        
        
        

@csrf_exempt

def SaveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name,file)
    return HttpResponse(file_name)