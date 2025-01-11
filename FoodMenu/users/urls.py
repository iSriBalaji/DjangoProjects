from django.urls import path
from . import views

app_name = 'users' #namespacing the app as menu so that can be used in URL in html files
urlpatterns = [
    path('register/', views.register,name='register'),
]