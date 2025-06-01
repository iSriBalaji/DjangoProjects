from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Menu
from django.template import loader
from .forms import AddForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     menu_items = Menu.objects.all()

#     context = {"menu_items":menu_items}
#     return render(request,'TheMenu/index.html',context)

# the above function based view as a good practivse can be defined in the class based view
# class based view follows the same way of connecting a url pattern to a view and defining the main logic in the view
# in class based actually - we have to do less things rather than writing more logic , ex: In Class list view once we provide the model name it will take care of itself automatically
class IndexClassView(ListView):
    model = Menu
    template_name = 'TheMenu/index.html'
    context_object_name = 'menu_items'

def home(request):
    # return render(request, 'TheMenu/index.html')
    return HttpResponse("Welcome to Home Page!")

def learn(request):
    return render(request, 'TheMenu/learn.html', {'message': 'Learn and Be disciplined'})

# def detail_item(request, item_id):
#     menu_item = Menu.objects.get(pk=item_id)
#     context = {"menu_item":menu_item}
#     return render(request,'TheMenu/item_detail.html',context)

# replacing the above detail view with the Detail view class
class IndexDetailView(DetailView):
    model = Menu
    template_name = 'TheMenu/item_detail.html'
    # context_object_name = 'menu_item'

def create_item(request):
    add_form = AddForm(request.POST or None)
    
    if add_form.is_valid():
        add_form.save()
        return redirect('menu:index')
    
    return render(request,'TheMenu/add_form.html',{'add_form':add_form, 'form_type':'Add Item'})


class CreateNewItem(CreateView):
    model = Menu
    fields = ['item', 'price', 'description', 'item_image']
    template_name = 'TheMenu/add_form.html'
    success_url = reverse_lazy('menu:index')

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        if not form.cleaned_data.get('item_image'):
            form.instance.item_image = 'https://cdn-icons-png.flaticon.com/512/2276/2276941.png'

        return super().form_valid(form)

    def form_invalid(self, form):
        print("FORM IS INVALID ❌")
        print(form.errors)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_type'] = 'Add Item'
        return context
    
# class CreateNewItem(CreateView):
#     model = Menu
#     fields = ['item', 'price', 'description', 'item_image']
#     template_name = 'TheMenu/add_form.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def update_item(request, item_id):
    # we are going to use the same form and update the value
    item_details = Menu.objects.get(pk=item_id)
    update_form = AddForm(request.POST or None, instance=item_details)
    
    if update_form.is_valid():
        if not update_form.cleaned_data.get('item_image'):
            item_details.item_image = 'https://cdn-icons-png.flaticon.com/512/2276/2276941.png'
        update_form.save()
        return redirect('menu:index')
    
    return render(request, 'TheMenu/add_form.html', {'add_form': update_form, 'form_type': 'Update Item'})

def delete_item(request, item_id):
    # here only when the request is of post type from the form we are performing the operation until then its just looping are staying in the same page
    # the html template for this should be a post request form and shoud submit>>
    item_details = Menu.objects.get(pk=item_id)
    
    if request.method == 'POST':
        item_details.delete()
        return redirect('menu:index')
    
    return render(request,'TheMenu/delete_item.html',{'item_details':item_details, 'form_type':'Delete Item'})

