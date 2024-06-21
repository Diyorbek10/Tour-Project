from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from.models import Agency
from .serializers import AgencySerializer


class AgencyListCreateAPIView(ListCreateAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    
    
class AgencyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer