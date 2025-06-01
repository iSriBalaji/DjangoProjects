from django.urls import path
from . import views

app_name = 'menu' #namespacing the app as menu so that can be used in URL in html files
urlpatterns = [
    path('', views.IndexClassView.as_view(),name='index'),
    path('home/', views.home,name='home'),
    path('<int:pk>/', views.IndexDetailView.as_view(),name='detail_item'), #here name is also important that identifies the url pattern that we can use in html files for rendering
    path('add', views.CreateNewItem.as_view(),name='create_item'),
    path('update/<int:item_id>', views.update_item,name='update_item'),
    path('delete/<int:item_id>', views.delete_item,name='delete_item'),
]