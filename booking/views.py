from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking
from .serializers import BookingSerializer

class BookingListCreateAPIView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
class BookingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer