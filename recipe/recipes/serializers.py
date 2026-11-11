from rest_framework import serializers
from recipes.models import recipe

class recipeserializer(serializers.ModelSerializer):
    class Meta:
        model=recipe
        fields="__all__"
