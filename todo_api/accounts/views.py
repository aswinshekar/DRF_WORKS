from django.shortcuts import render
from rest_framework.views import APIView

from accounts.serializers import UserSerializer
# Create your views here.
#register api
from rest_framework import status
from rest_framework.response import Response
class RegisterAPI(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)#tile,description,completed
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
