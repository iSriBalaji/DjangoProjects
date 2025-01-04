from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'TheMenu/index.html')

def learn(request):
    return render(request, 'TheMenu/learn.html', {'message': 'Learn and Be disciplined'})

