from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from food.models import Food
from .forms import CreateForm 
# Create your views here.

# function based view
def first_view(request):
    """
    A function-based view that returns an HttpResponse with a greeting message.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: An HTTP response with a greeting message.

    Examples:
        >>> response = first_view(request)
        >>> response.content
        b'<h1>Hii all, successfully I created my first djnago function based view without taking the help of any tutorial. A big Thanks to google teacher and the official docs of django</h1>'
    """
    return HttpResponse("<h1>Hii all, successfully I created my first djnago function based view\
                        without taking the help of any tutorial.\
                        A big Thanks to google teacher and the official docs of django</h1>")

@login_required()
def create(request):
    """
    A view that handles the creation of a new food item.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse or HttpResponseRedirect: If the request method is POST and the form data is valid, it saves the form data and redirects to the 'food:show' URL. Otherwise, it renders the 'food/add_food.html' template with the form.

    Examples:
        >>> response = create(request)
        >>> response.status_code
        200
    """
    form_data = CreateForm(request.POST or None)
    if request.method == 'POST' and form_data.is_valid():
        form_data.save()
        return redirect('food:show')

    return render(request, 'food/add_food.html', {'food': form_data})


def show(request):
    """
    A view that displays all food items.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: An HTTP response that renders the 'food/show.html' template with the list of food items.

    Examples:
        >>> response = show(request)
        >>> response.status_code
        200
    """
    items = Food.objects.all()
    paginator = Paginator(items, 2, 1, False)

    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    
    context = {
        "items": page_obj
    }

    return render(request, 'food/show.html', context)

def details(request, id):
    if item_details := Food.objects.get(id=id):
        return render(request, 'food/details.html', {'details': item_details})
    
@login_required()
def delete_item(request, id):

    obj = get_object_or_404(Food, id = id)
    if request.method == "POST":
        query = Food.objects.get(id = id)
        query.delete()
        return redirect('food:show')

    return render(request, 'food/delete.html', {'item': obj})

@login_required()
def update_item(request, id):
    item_obj = get_object_or_404(Food, id =id)

    form = CreateForm(request.POST or None, instance=item_obj)

    if form.is_valid():
        form.save()
        return redirect('food:show')
    
    return render(request, 'food/update.html', {"item": form})

def search_view(request):

    context = {}
    if request.method == "POST":
        search_item = request.POST.get('search_query')
        result_item = Food.objects.filter(name__icontains = search_item)
        context["items"] = result_item
        return render(request, 'food/show.html', context=context)
    
    return render(request, 'food/base.html', context=context)

    
