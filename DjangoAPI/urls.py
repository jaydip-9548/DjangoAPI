
from django.contrib import admin
from django.urls import path,re_path,include
# from django.conf.urls import url,include
from django.views.generic import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('emp.urls')),
    path('',TemplateView.as_view(template_name='index.html'))
]
