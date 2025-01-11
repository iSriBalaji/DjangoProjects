from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Menu
from django.template import loader
from .forms import AddForm

# Create your views here.
def index(request):
    menu_items = Menu.objects.all()

    context = {"menu_items":menu_items}
    return render(request,'TheMenu/index.html',context)

def home(request):
    # return render(request, 'TheMenu/index.html')
    return HttpResponse("Welcome to Home Page!")

def learn(request):
    return render(request, 'TheMenu/learn.html', {'message': 'Learn and Be disciplined'})

def detail_item(request, item_id):
    menu_item = Menu.objects.get(pk=item_id)
    context = {"menu_item":menu_item}
    return render(request,'TheMenu/item_detail.html',context)

def create_item(request):
    add_form = AddForm(request.POST or None)
    
    if add_form.is_valid():
        add_form.save()
        return redirect('menu:index')
    
    return render(request,'TheMenu/add_form.html',{'add_form':add_form, 'form_type':'Add Item'})

def update_item(request, item_id):
    #we are going to use the same form and update the value
    item_details = Menu.objects.get(pk=item_id)
    update_form = AddForm(request.POST or None, instance=item_details)
    
    if update_form.is_valid():
        update_form.save()
        return redirect('menu:index')
    
    return render(request,'TheMenu/add_form.html',{'add_form':update_form, 'form_type':'Update Item'})

def delete_item(request, item_id):
    # here only when the request is of post type from the form we are performing the operation until then its just looping are staying in the same page
    # the html template for this should be a post request form and shoud submit>>
    item_details = Menu.objects.get(pk=item_id)
    
    if request.method == 'POST':
        item_details.delete()
        return redirect('menu:index')
    
    return render(request,'TheMenu/delete_item.html',{'item_details':item_details, 'form_type':'Delete Item'})

