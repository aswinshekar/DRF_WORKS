from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from accounts.serializers import UserSerializer
from reviews.models import Review
from recipes.serializers import recipeserializer

class ReviewSerializer(serializers.ModelSerializer):
    # # NESTED SERIALIZER
    # user=UserSerializer()
    # recipe=recipeserializer()
    # #DISPLAY THE ALL FIELDS OF THE RELATED DATA
    user=StringRelatedField()
    recipe=StringRelatedField()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model=Review
        # fields="__all__"
        exclude = ['id']
        read_only_fields=['user','created']


