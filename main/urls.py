from django.urls import path, include
from django.views.generic.detail import DetailView
from . import views
from main import models

app_name = 'main'

urlpatterns = [


    path('products/<slug:tag>/', views.ProductListView.as_view(), name="products", ),
    path("product/<slug:slug>/", DetailView.as_view(model=models.Product), name="product", ),
]
