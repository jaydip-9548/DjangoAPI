from django.contrib import admin
from django.urls import path,re_path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('getdeptApi/',views.department_detail,name='department_detail'),
    path('getempApi/',views.employee_detail,name='employee_detail'),
    path('emp/SaveFile/',views.SaveFile,name='SaveFile'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
