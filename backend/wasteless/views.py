from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView
from django.views import generic

from .models import List
from .forms import ListItemForm


# Create your views here.
def index(request):
    return render(request, 'home.html')


class ListView(generic.ListView):
    model = List
    template_name = 'lists.html'


def list_view(request, list_id):
    crt_list = get_object_or_404(List, pk=list_id)
    list_items = crt_list.listitem_set.all()

    context = {
        'list': crt_list,
        'listitems': list_items,
        'form': ListItemForm()
    }
    return render(request, 'list_detail.html', context)


def list_add_item(request, list_id):
    if request.method == 'POST':
        form = ListItemForm(request.POST)
        list_item = form.save(commit=False)
        list_item.parent_list_id = list_id
        list_item.save()

        return redirect(f'/list/{list_id}')

    return render(request, 'base.html')


class ListCreate(CreateView):
    model = List
    fields = ['name']
    template_name = 'create_list.html'
