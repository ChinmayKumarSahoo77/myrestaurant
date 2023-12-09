from django.urls import path

from .views import first_view, create

urlpatterns = [
    path("",first_view, name= 'first_view'),
    path("add/",create, name= 'create'),
]