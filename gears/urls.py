from django.urls import path
from . import views

urlpatterns = [
    path('gears/', views.gears, name="gears")
]
