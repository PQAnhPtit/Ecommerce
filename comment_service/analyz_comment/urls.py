from django.urls import path
from . import views

urlpatterns = [
    path('reviewcm/', views.analyze_review, name='reviewcm'),
]
