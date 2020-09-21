from django.urls import path
from . import views

urlpatterns = [
    path('', views.AirplaneListAPIView.as_view(), name='airplane_list'),
    path('airplanes/<int:pk>/', views.AirplaneDetailAPIView.as_view(), name='airplane_detail'),
]