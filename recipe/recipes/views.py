from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from recipes.models import recipe
from recipes.serializers import recipeserializer
# Create your views here.
class RecipeCreate(APIView):
    def post(self,request):
        serializer_instance=recipeserializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class RecipeList(APIView):
    def get(self,request):
        qs=recipe.objects.all()
        serializer_instance=recipeserializer(qs,many=True)
        return Response(serializer_instance.data)
class RecipeView(APIView):
    def get(self,request,i):
        r=get_object_or_404(recipe,id=i)
        serializer_instance=recipeserializer(r)
        return Response(serializer_instance.data)
class RecipeUpdate(APIView):
    def put(self,request,i):
        r=get_object_or_404(recipe,id=i)
        serializer_instance=recipeserializer(instance=r,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class RecipePartialUpdate(APIView):
    def patch(self,request,i):
        r=get_object_or_404(recipe,id=i)
        serializer_instance=recipeserializer(instance=r,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class RecipeDelete(APIView):
    def delete(self,request,i):
        r=get_object_or_404(recipe,id=i)
        r.delete()
        return Response({"message":"DELETED"})



