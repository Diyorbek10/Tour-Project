from django.urls import path
from .views import *

urlpatterns = [
    path('',BookingListCreateAPIView.as_view()),
    path('<int:pk>/',BookingRetrieveUpdateDestroyAPIView.as_view())
]