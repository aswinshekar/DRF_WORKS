from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Model, Q
from django.shortcuts import  get_object_or_404
from rest_framework import status, response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from doctors.serializers import DoctorSerializer
from doctors.serializers import UserSerializer
from doctors.models import Doctor

# Create your views here.
#API VIEWS FOR CREATING DOCTOR
#API VIEWS FOR READING ALL DOCTORS
class DoctorListCreateView(APIView):
    authentication_classes = [BasicAuthentication]  # username,password
    permission_classes = [IsAdminUser]

    def get(self, request):
        d = Doctor.objects.all()
        serializer_instance = DoctorSerializer(d, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer_instance = DoctorSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)



class RetrieveUpdateDelete(APIView):
    authentication_classes = [BasicAuthentication]  # username,password
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        d = get_object_or_404(Doctor, id=pk)
        serializer_instance = DoctorSerializer(d)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        d = get_object_or_404(Doctor, id=pk)
        serializer_instance = DoctorSerializer(instance=d, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        d = get_object_or_404(Doctor, id=pk)
        d.delete()
        return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)




#API VIEWS FOR READING A SPECIFIC DOCTOR
#API VIEWS FOR UPDATING A DOCTOR
#API VIEWS FOR DELETING A DOCTOR
#API VIEWS FOR FILTERING DOCTORS BASED ON SPECIFICATIONS

#FILTERING DOCTOR BASED ON SPECIALIZATION
class DoctorFilter(APIView):
    def get(self,request):
        data=request.query_params.get('search')
        d=Doctor.objects.filter(specialization=data)
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
# from rest_framework import UserSerializer

#APIVIEW FOR CREATING A ADMIN USER
class AdminRegiser(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


