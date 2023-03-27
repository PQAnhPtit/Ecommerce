from django.urls import path
from . import views

urlpatterns = [
    path('addorder/', views.add_order_data, name='addorder'),
    path('deleteorder/<str:id>/', views.delete_order_data, name='deleteorder'),
]
