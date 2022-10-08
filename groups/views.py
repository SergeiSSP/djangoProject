from django.http import HttpResponseRedirect, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

from groups.forms import CreateGroupForm, UpdateGroupForm
from groups.models import Group


def get_groups(request):
    groups = Group.objects.all()
    return render(
        request,
        'groups/list.html',
        context={
            'title': 'list of groups',
            'groups': groups
        }
    )


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == "POST":
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students')

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



def detailed_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    return render(
        request,
        'groups/details.html',
        context={
            'group': group,
            'title': group.name,
        }

    )




def update_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/groups')

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