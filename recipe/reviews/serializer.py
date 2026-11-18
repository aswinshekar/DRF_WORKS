from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from accounts.serializers import UserSerializer
from recipes.models import recipe
from reviews.models import Review
from recipes.serializers import recipeserializer

class ReviewSerializer(serializers.ModelSerializer):
    # # NESTED SERIALIZER
    # user=UserSerializer()
    # recipe=recipeserializer()
    # #DISPLAY THE ALL FIELDS OF THE RELATED DATA
    # #STRINGRELATEDFIELD
    # user=StringRelatedField()
    # recipe=StringRelatedField()
    # #DISPLAYS THE RELATED OBJECTS USING ITS STRING REPRESENTATION DEFINED INSIDE STR
    # #__str__()
    message=serializers.SerializerMethodField()

    user=serializers.SerializerMethodField()
    recipe=serializers.SerializerMethodField()
    created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model=Review
        # fields="__all__"
        exclude = ['id']
        read_only_fields=['user','created']
    def get_message(self,obj):
        return "hello"
    def get_recipe(self,obj):
        return obj.recipe.recipe_name
    def get_user(self,obj):
        return obj.user.email


