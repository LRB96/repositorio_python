from django.urls import path
from . import views

urlpatterns = [
    path('', hello),
    path('about/', about)
]