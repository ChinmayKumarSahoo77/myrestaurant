from django.shortcuts import render
from django.http import HttpResponse
from food.models import Food
from .forms import CreateForm 
# Create your views here.

# function based view
def first_view(request):
    return HttpResponse("<h1>Hii all, successfully I created my first djnago function based view\
                        without taking the help of any tutorial.\
                        A big Thanks to google teacher and the official docs of django</h1>")


def create(request):
    form_data = CreateForm(request.POST or None)
    if request.method == 'POST' and form_data.is_valid():
            form_data.save()

    context = {
        'food': form_data
    }
    return render(request, 'food/add_food.html', context)