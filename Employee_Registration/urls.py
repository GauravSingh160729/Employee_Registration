"""
URL configuration for Employee_Registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Employee_Form import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add', views.add_show, name='addandshow'),
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),
    path('update/<int:id>/', views.update_employee, name='update_employee'),  # New route
]

