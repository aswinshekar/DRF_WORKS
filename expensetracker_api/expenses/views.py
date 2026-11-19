from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.templatetags import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from expenses.serializer import ExpenseSerializer
from rest_framework import status

# Create your views here.
class ExpenseCreate(APIView):
    authentication_classes = [TokenAuthentication]#to check whether user is valid
    permission_classes = [IsAuthenticated] #only logged in can create expense
    def post(self,request):
        serializer_instance=ExpenseSerializer(data=request.data)#all fields expect user
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.erros,status=status.HTTP_400_BAD_REQUEST)


