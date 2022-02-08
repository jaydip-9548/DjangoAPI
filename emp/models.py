from django.db import models

# Create your models here.

class DepartmentData(models.Model):
    dept_id = models.BigAutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=50)


class EmployeeData(models.Model):
    emp_id = models.BigAutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=50)
    DepartmentName = models.CharField(max_length=50)
    DateOfJoining = models.DateField()
    PhotoName = models.CharField(max_length=100)
