from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from app import serializers
from app.models import Student
from app.serializers import StudentSerializer

class StudentCreate(APIView):
    def post(self,request):
        data=request.data
        serializer_instance=StudentSerializer(data=data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response (serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class StudentViews(APIView):
    def get(self,request):
        qs=Student.objects.all()
        serializer_instance=StudentSerializer(qs,many=True)
        return Response(serializer_instance.data)
class Studentview(APIView):
    def get(self,request,i):
        e=get_object_or_404(Student,id=i)
        serializer_intance=StudentSerializer(e)

        return Response(serializer_intance.data)

class StudentUpdate(APIView):
    def put(self,request,i):
        e=get_object_or_404(Student,id=i)
        serializer_instance=StudentSerializer(instance=e,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response (serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class StudentPartialUpdate(APIView):
    def patch(self,request,i):
        e=get_object_or_404(Student,id=i)
        serializer_instance=StudentSerializer(instance=e,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response (serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
class StudentDelete(APIView):
    def delete(self,request,i):
        e = get_object_or_404(Student,id=i)
        e.delete()
        return Response ({"message":"Deleted"})


