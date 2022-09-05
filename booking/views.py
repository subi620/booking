from django.shortcuts import render
from rest_framework import generics
from .models import Booking
from .serializer import BookingSerializer
# Create your views here.

class BookingList(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


