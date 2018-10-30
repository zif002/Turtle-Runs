from django.shortcuts import render

# Create your views here.
from .models import Turtle, Cards
from rest_framework import viewsets
from .serializers import TurtleSerializer, CardsSerializer


class TurtleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Turtle.objects.all()
    serializer_class = TurtleSerializer


class CardsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cards.objects.all()
    serializer_class = CardsSerializer