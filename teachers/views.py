from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from teachers.forms import CreateTeacherForm, UpdateTeacherForm
from teachers.models import Teacher


def get_teachers(request):
    teachers = Teacher.objects.all()
    return render(
        request,
        'teachers/list.html',
        context={
            'title': 'List of teachers',
            'teachers': teachers
        }
    )


def create_teacher(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(Teacher, 'teacher:list'))
    return render(
        request,
        'teachers/create.html',
        {'form': form}
    )


def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers')

    return render(
        request,
        'students/update.html',
        {'form': form}
    )

def detailed_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(
        request,
        'teachers/details.html',
        {'teacher': teacher}
    )

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teacher:list'))

    if request.method == 'GET':
        return render(
            request,
            'teachers/delete.html',
            {'teacher': teacher},
        )