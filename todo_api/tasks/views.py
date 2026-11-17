import selectors

from MySQLdb.constants.ER import MIXING_NOT_ALLOWED
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks import serializers
from tasks.models import Task
from tasks.permissions import IsOwner
from tasks.serializers import TaskSerializers

# Create your views here.
# using APIVIEW
# class TaskListCreate(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         t=Task.objects.filter(user=request.user)
#         serializer_instance=TaskSerializers(t,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer_instance=TaskSerializers(data=request.data)#tile,description,completed
#         if serializer_instance.is_valid():
#             serializer_instance.save(user=request.user)
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
# USING MIXING
from rest_framework import generics
class TaskListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class=TaskSerializers
    queryset=Task.objects.all()

    # to add custom logic inside generics view we overide get_queryset()
    # and perform_Create()
    # for creation->perform_create()
    # for list->get_queryset()

    def get_queryset(self):#for query set
        return Task.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetriveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]
    def get(self,request,pk):
        t=get_object_or_404(Task,id=pk)
        serializer_instance=TaskSerializers(t)
        return Response(serializer_instance.data,status=status.HTTP_404_NOT_FOUND)
    def put(self,request,pk):
        t = get_object_or_404(Task, id=pk)
        serializer_instance = TaskSerializers(instance=t,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        t = get_object_or_404(Task, id=pk)
        t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

