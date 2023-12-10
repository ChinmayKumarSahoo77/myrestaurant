from django.urls import path

from .views import first_view, create, show, details

app_name = 'food'
urlpatterns = [
    path("",first_view, name= 'first_view'),
    path("add/",create, name= 'create'),
    path("all/", show, name='show'),
    path("<int:id>", details, name='details'),
]