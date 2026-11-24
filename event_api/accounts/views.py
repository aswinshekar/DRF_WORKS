from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.serializers import CustomUserSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class RegisterAPI(APIView):
    def post(self,request):
        serializer_instance=CustomUserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response (serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        request.user.auth_token.delete()
        return Response({'message':"Logout Succefull"},status=status.HTTP_200_OK)