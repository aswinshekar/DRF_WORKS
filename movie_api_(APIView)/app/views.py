from django.db.migrations import serializer
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response

from app.serializers import MovieSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from app.models import Movie


# Create your views here.


#for creating a new movie record:

class MovieCreate(APIView):
    def post(self,request):

        serializer_instance=MovieSerializer(data=request.data)#deserializeation
        if serializer_instance.is_valid():
            # print(serializer_instance.validated_data)
            # director=serializer_instance.validated_data['director']
            # print(director)
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
#READING ALL MOVIE RECORDS
class MovieView(APIView):
    def get(self,request):
        qs=Movie.objects.all()
        serializer_instance=MovieSerializer(qs,many=True)
        return Response(serializer_instance.data)
#READING A SPECIFIC RECORD
class MovieViewSpecific(APIView):
    def get(self,request,i):
        s=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(s)
        return Response(serializer_instance.data)
#API CODE FOR DELETEING RECORD
class MovieDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Movie,id=i)
        e.delete()
        return Response("message: RECORD DELETED SUCCESFULLY")
#API CODE FOR UPDATING A RECORD

class MovieUpdate(APIView):
    def put(self,request,i):
        e=get_object_or_404(Movie,id=i)
        data=request.data
        serializer_instance=MovieSerializer(instance=e,data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

#UPDATING A SPECIFIC RECORD

class MoviePartialUpdate(APIView):
    def patch(self,request,i):
        e=get_object_or_404(Movie,id=i)
        data=request.data
        serializer_instance=MovieSerializer(instance=e,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
from django.db.models import Q
class SearchAPIView(APIView):
    def get(selfself,request):
        data=request.query_params.get('search')
        print(data)
        m=Movie.objects.filter(Q(title__icontains=data)|
                               Q(director__icontains=data)|
                               Q(language__icontains=data)|
                               Q(year__icontains=data))
        #filter
        #field lookups
        #Q
        serializer_instance=MovieSerializer(m,many=True)


        return Response(serializer_instance.data)



from app.serializers import UserSerializer

class RegisterView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)#deserializeation
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
from rest_framework import status
class RegisterAPIView(APIView):
    def post(self, request):
        serializer_instance = UserSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                serializer_instance.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                serializer_instance.errors,
                status=status.HTTP_400_BAD_REQUEST
            )