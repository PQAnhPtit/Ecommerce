from django.urls import path
from . import views

urlpatterns = [
    path('getbook/', views.get_book_data, name='getbook'),
]
