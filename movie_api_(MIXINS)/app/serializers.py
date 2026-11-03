from django.db.models import Model
from rest_framework import serializers
from django.db import models
from app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ['title', 'director', 'language', 'year', 'runtime', 'rating','image']