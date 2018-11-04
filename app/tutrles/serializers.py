from .models import Turtle, Cards
from rest_framework import serializers

class TurtleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turtle
        fields = ('name', 'color', 'id_thurtle')


class CardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cards
        fields = ('name', 'color', 'diraction', 'count_step')