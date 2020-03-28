from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_list', views.ListCreate.as_view(), name='create_list')
]
