"""
URL configuration for FoodMenu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
from users.views import user_logout, register, profilepage
from django.conf import settings
from django.conf.urls.static import static # to use the static files - we used it for displating profile image



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('TheMenu.urls')),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # this is a class based view
    path('logout/', user_logout, name='logout'),
    path('profile/', profilepage, name='profile'),
    # path('/', HttpResponse("Welcome to Home Page!")),
]

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # when i changed to media url and media root it worked