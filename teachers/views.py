from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

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
            return HttpResponseRedirect('/teachers')
    token = get_token(request)
    html_form = f'''
                <form method='post'>
                <input type = 'hidden' name = 'csrfmiddlewaretoken' value = '{token}'>
                    <table>
                        {form.as_table()}
                    </table>
                    <input type="submit" value="Submit">
                </form> 
            '''
    return HttpResponse(html_form)


def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers')

    token = get_token(request)
    html_form = f'''
            <form method='post'>
            <input type = 'hidden' name = 'csrfmiddlewaretoken' value = '{token}'>
                <table>
                    {form.as_table()}
                </table>
                <input type="submit" value="Update">
            </form> 
        '''
    return HttpResponse(html_form)


def detailed_teacher(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(
        request,
        'teachers/details.html',
        {'teacher': teacher}
    )
