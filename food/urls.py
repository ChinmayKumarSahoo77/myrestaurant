from django.urls import path

from .views import first_view, create, show, details, delete_item, update_item, search_view

app_name = 'food'
urlpatterns = [
    path("",first_view, name= 'first_view'),
    path("add/",create, name= 'create'),
    path("all/", show, name='show'),
    path("<int:id>", details, name='details'),
    path("delete/<int:id>", delete_item, name='delete'),
    path("update/<int:id>", update_item, name='update_item'),
    path('search/', search_view, name='search'),
]