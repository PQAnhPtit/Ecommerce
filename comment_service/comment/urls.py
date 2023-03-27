from django.urls import path
from . import views

urlpatterns = [
    path('addcomment/', views.add_comment_data, name='addcomment'),
]
