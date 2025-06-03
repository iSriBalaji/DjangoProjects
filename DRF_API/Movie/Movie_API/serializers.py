from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    poster = serializers.ImageField(max_length = None, use_url = True)
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating', 'genre', 'poster']

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating']