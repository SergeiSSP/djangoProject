from django.urls import path

from students.views import create_student, detailed_student, delete_student
from students.views import get_students
from students.views import update_student

app_name = 'student'

urlpatterns = [
    path('', get_students, name="list"),
    path('create/', create_student, name='create'),
    path('update/<int:student_id>/', update_student, name='update'),
    path('detail/<int:student_id>/', detailed_student, name='detailed'),
    path('delete/<int:student_id>/', delete_student, name="delete"),

]