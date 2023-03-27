from django.urls import path
from . import views

urlpatterns = [
    path('addimg/', views.add_img_data, name='addimg'),
]
