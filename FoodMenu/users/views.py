from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def register(request):
    # only when http request is post otherwise render the usual form, need to understand this
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # will have all the data from the post request
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('menu:index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})