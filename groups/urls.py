from django.urls import path

from groups.views import get_groups, create_group, detailed_group, update_group, delete_group

app_name = 'group'
urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('detail/<int:group_id>/', detailed_group, name='detail'),
    path('update/<int:group_id>/', update_group, name='update'),
    path('delete/<int:group_id>/', delete_group, name='delete'),
]
