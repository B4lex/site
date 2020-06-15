from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarsList.as_view(), name='cars_list'),
    path('car/<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
    path('update/', views.CarsUpdate.as_view(), name='cars_update'),
]

