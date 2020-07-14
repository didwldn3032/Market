from django.urls import path 
from .views import new, create, main
from .views import main, new, create, show 

app_name = "posts" 
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    path('/show/<int:id>', show, name="show"),
    ]