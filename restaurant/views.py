from django.shortcuts import render
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer

# imports for API
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# class BookingView(APIView):
    
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data) # Return JSON

#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})

# class MenuView(APIView):
    
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuSerializer(items, many=True)
#         return Response(serializer.data) # Return JSON

#     def post(self, request):
#         serializer = MenuSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})

class MenuItemView(ListCreateAPIView):

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    """
    GET, PUT, and DELETE
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    
    
