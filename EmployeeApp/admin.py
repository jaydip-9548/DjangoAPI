from django.contrib import admin
from .models import DepartmentData,EmployeeData

# Register your models here.
admin.site.register(DepartmentData)
admin.site.register(EmployeeData)