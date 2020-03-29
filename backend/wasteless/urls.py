from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_list', views.ListCreate.as_view(), name='create_list'),
    path('list/<int:list_id>', views.list_view, name='list_view'),
    path('list/<int:list_id>/add-item', views.list_add_item, name='list_add_item'),
    path('lists', views.ListView.as_view(), name='lists')
]
