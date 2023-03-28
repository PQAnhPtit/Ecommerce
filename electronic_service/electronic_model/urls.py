from django.urls import path
from . import views

urlpatterns = [
    path('getelectronic/', views.get_electronic_data, name='getelectronic'),
]
