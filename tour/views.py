from django.shortcuts import render
from .serializers import CategorySerializer,TourSerializer,TourServiceSerializer, MeadiTourSerializer,FeedbackSerializer
from .models import Category,Tour,TourService,MediaTour,Feedback
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class TourListCreateApiView(ListCreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
 
    
class TourRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
 
    
class TourServiceListCreateAPIView(ListCreateAPIView):
    queryset = TourService.objects.all()
    serializer_class = TourServiceSerializer
  
    
class TourServiceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TourService.objects.all()
    serializer_class = TourServiceSerializer
  
    
class MeadiTourListCreateAPIView(ListCreateAPIView):
    queryset = MediaTour.objects.all()
    serializer_class = MeadiTourSerializer
  
    
class MeadiTourRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MediaTour.objects.all()
    serializer_class = MeadiTourSerializer


class FeedbackListCreateAPIView(ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
 
    
class FeedbackRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer