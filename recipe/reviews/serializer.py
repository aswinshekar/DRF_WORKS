from rest_framework import serializers

from accounts.serializers import UserSerializer
from reviews.models import Review
from recipes.serializers import recipeserializer

class ReviewSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    recipe=recipeserializer()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model=Review
        # fields="__all__"
        exclude = ['id']
        read_only_fields=['user','created']


