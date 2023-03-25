from django.urls import path
from . import views

urlpatterns = [
    path('getuser/', views.get_user_data, name='getuser'),
    path('userregistration/', views.registration_req, name='userregistration'),
]
