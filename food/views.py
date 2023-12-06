from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# function based view
def first_view(request):
    return HttpResponse("<h1>Hii all, successfully I created my first djnago function based view\
                        without taking the help of any tutorial.\
                        A big Thanks to google teacher and the official docs of django</h1>")