from django.urls import path
from . import views

app_name="homepage"
urlpatterns=[
    path('',views.main, name="main"),
    path('food/',views.food, name="food"),
    path('fashion/',views.fashion, name="fashion"),
    path('delivery/',views.delivery, name="delivery"),    
]