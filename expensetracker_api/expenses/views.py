from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.templatetags import rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response

from expenses import serializer
from expenses.serializer import ExpenseSerializer
from rest_framework import status

from expenses.permission import IsOwner


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
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
from expenses.models import Expense
class ExpenseList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        e=Expense.objects.filter(user=request.user)#filters only current user expenses
        serializer_instance=ExpenseSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class ExpenseRetrive(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]
    def get(self,request,pk):
        r=get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request,r)
        serializer_instance=ExpenseSerializer(r)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class ExpenseDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    def delete(self, request, pk):
        r = get_object_or_404(Expense,id=pk)
        self.check_object_permissions(request, r)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExpenseUpdate(APIView):
    authentication_classes = [TokenAuthentication]#to check whether user is valid
    permission_classes = [IsAuthenticated,IsOwner] #only logged in can create expense
    def put(self,request,pk):
        r = get_object_or_404(Expense, id=pk)
        serializer_instance=ExpenseSerializer(instance=r,data=request.data)#all fields expect user
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



