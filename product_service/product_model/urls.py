from django.urls import path
from . import views

urlpatterns = [
    # path('getproduct/', views.get_product_data, name='getproduct'),
    # path('addproduct/', views.add_product_data, name='addproduct'),
    # path('deleteproduct/<str:product_id>/', views.delete_product_data, name='deleteproduct'),
    # path('updateproduct/<str:product_id>/', views.update_product_data, name='updateproduct'),
    path('getbookdata/', views.get_book, name='getbookdata'),
    path('getclothedata/', views.get_clothe, name='getclothedata'),
    path('getshoedata/', views.get_shoe, name='getshoedata'),
    path('getelectronicdata/', views.get_electronic, name='getelectronicdata'),
]
