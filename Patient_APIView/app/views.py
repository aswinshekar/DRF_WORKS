from django.db.models import Model
from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from app import serializers
from app.models import Patient
from app.serializers import PatientSerializer

class PatientCreate(APIView):
    def post(self,request):
        serializer_instance=PatientSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class PatientList(APIView):
    def get(self,request):
        qs=Patient.objects.all()
        serializer_instance=PatientSerializer(qs,many=True)
        return Response(serializer_instance.data)

class PatientView(APIView):
    def get(self,request,i):
        p=get_object_or_404(Patient,patient_id=i)
        serializers_instacne=PatientSerializer(p)
        return Response(serializers_instacne.data)

class PatientUpdate(APIView):
    def put(self,request,i):
        p=get_object_or_404(Patient,patient_id=i)
        serializer_instance=PatientSerializer(instance=p,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


class PatientPartialUpdate(APIView):
    def patch(self, request, i):
        p = get_object_or_404(Patient, patient_id=i)
        serializer_instance = PatientSerializer(instance=p, data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class PatientDelete(APIView):
    def delete(self, request, i):
        p = get_object_or_404(Patient, patient_id=i)
        p.delete()
        return Response({"message":"Deleted"})




