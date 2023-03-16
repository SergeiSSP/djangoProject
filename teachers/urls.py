from django.urls import path

from .views import get_teachers, create_teacher
from .views import update_teacher, detailed_teacher, delete_teacher
app_name = 'teacher'

urlpatterns = [
path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
    path('detail/<int:teacher_id>/', detailed_teacher, name='detail'),
    path('delete/<int:teacher_id>', delete_teacher, name='delete'),
]
