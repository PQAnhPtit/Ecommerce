from django.urls import path
from . import views

urlpatterns = [
    path('getcloth/', views.get_cloth_data, name='getcloth'),
]
