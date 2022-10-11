from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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
            return HttpResponseRedirect(reverse(Group, 'group:list'))

    return render(
        request,
        'groups/create.html',
        {'form': form},
    )


def detailed_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    return render(
        request,
        'groups/details.html',
        context={
            'group': group,
            'title': group.name,
        }

    )


def update_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('group:list'))

    return render(
        request,
        'groups/update.html',
        {'form': form}
    )

def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)

    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('group:list'))

    if request.method == 'GET':
        return render(
            request,
            'groups/delete.html',
            {'group': group}
        )
