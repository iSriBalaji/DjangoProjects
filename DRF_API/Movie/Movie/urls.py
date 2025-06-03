from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Movie_API.views import MovieViewSet, ActionViewSet, ComedyViewSet, list_movie
from django.conf.urls.static import static
from django.conf import settings

router = routers.SimpleRouter()
router.register('movies', MovieViewSet, basename='movies')
router.register('action', ActionViewSet, basename='action')
router.register('comedy', ComedyViewSet, basename='comedy')

urlpatterns = [
    path('api/', include(router.urls)), 
    path('admin/', admin.site.urls),
    path('list/', list_movie, name='list_movie'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
