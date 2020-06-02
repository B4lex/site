from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarsList.as_view(), name='car'),
]

