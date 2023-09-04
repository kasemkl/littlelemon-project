from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import *
from .serializer import *
from rest_framework import permissions
# Create your views here.
class MenuView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
    
class SingleMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
class BookingsViewSet(viewsets.ModelViewSet):
    queryset=Bookings.objects.all()
    serializer_class=BookingSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 