from django.urls import path
from . import views

urlpatterns = [
    path('', views.basket, name="basket"),
    path('add/<item_id>/', views.add_to_basket, name="add_to_basket"),
    path('update/<item_id>/', views.update_basket, name="update_basket"),
    path('remove/<item_id>/', views.remove_basket, name="remove_basket"),
]
