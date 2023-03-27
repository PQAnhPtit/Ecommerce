from django.urls import path
from . import views

urlpatterns = [
    path('addcart/', views.add_cart_data, name='addcart'),
    path('deletecart/<str:id>/', views.delete_cart_data, name='deletecart'),
]
