from django.shortcuts import render
from rest_framework import generics, viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Booking, Booking_Family, Booking_Marriage,Services, Rooms 
from .serializers import User, UserSerializer,RoomsSerializer, ServicesSerializer, BookingSerializer, Booking_MarriageSerializer, Booking_FamilySerializer
from .pagination import MenuPagination

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MenuPagination


class RoomsView(generics.ListCreateAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MenuPagination

class SingleRoomView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    permission_classes = [IsAuthenticated]

class ServicesView(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MenuPagination

class SingleServiceView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = [IsAuthenticated]


class BookingView(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = MenuPagination
    # permission_classes = [IsAuthenticated] 

class Booking_MarriageView(viewsets.ModelViewSet):
    queryset = Booking_Marriage.objects.all()
    serializer_class = Booking_MarriageSerializer
    pagination_class = MenuPagination
    # permission_classes = [IsAuthenticated]

class Booking_FamilyView(viewsets.ModelViewSet):
    queryset = Booking_Family.objects.all()
    serializer_class = Booking_FamilySerializer
    pagination_class = MenuPagination
    # permission_classes = [IsAuthenticated]
    