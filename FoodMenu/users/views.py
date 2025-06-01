from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    # only when http request is post otherwise render the usual form, need to understand this
    if request.method == 'POST': # we are checking if the request is a POST request - it will be post only if there are message posted from the form
        form = RegisterForm(request.POST) # will have all the data from the post request
        if form.is_valid(): #duplicate usernames and otherthings are automatically handled in the validation
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')