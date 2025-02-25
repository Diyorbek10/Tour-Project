from django.urls import path
from .views import AgencyListCreateAPIView,AgencyRetrieveUpdateDestroyAPIView,RegisterView,LoginView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('agency/',AgencyListCreateAPIView.as_view()),
    path('agency/<int:pk>/',AgencyRetrieveUpdateDestroyAPIView.as_view())
]