from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from.models import Agency,CustomUser
from .serializers import AgencySerializer,UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status 
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken



class AgencyListCreateAPIView(ListCreateAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    
    
class AgencyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
    
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    
class LoginView(APIView):
    def post(self,request):
        print(AccessToken())
        email = request.data['email']
        password = request.data['password']
        
        user = CustomUser.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed("User not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        return Response({"message":"Succes"})