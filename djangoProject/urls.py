"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import  include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.views import index
from groups.views import get_groups, create_group, detailed_group, update_group

from teachers.views import get_teachers, create_teacher, update_teacher, detailed_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('groups/', get_groups),
    path('groups/create/', create_group),
    path('groups/detail/<int:group_id>/', detailed_group),
    path('groups/update/<int:group_id>/', update_group),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher),
    path('teachers/update/<int:teacher_id>/', update_teacher),
    path('teachers/detail/<int:teacher_id>/', detailed_teacher),

]
