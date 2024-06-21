from django.urls import path
from .views import AgencyListCreateAPIView,AgencyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('agency/',AgencyListCreateAPIView.as_view()),
    path('agency/<int:pk>/',AgencyRetrieveUpdateDestroyAPIView.as_view())
]