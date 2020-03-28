from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import List


# Create your views here.
def index(request):
    return render(request, 'home.html')


class ListCreate(CreateView):
    model = List
    fields = ['name']
    template_name = 'create_list.html'


def create_list(request):
    return render(request, 'create_list.html')
