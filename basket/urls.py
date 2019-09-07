from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.manage_basket, name="basket"),
    path('add_to_basket/', views.add_to_basket, name="add_to_basket", ),

]
