from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.views import APIView
from django.db.models import Model, Q
from django.shortcuts import  get_object_or_404
from rest_framework import status, response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from patients.serializers import UserSerializer

from doctors.models import Doctor
# Create your views here.
#API VIEWS FOR CREATING DOCTOR
#API VIEWS FOR READING ALL DOCTORS

#API VIEW FOR APPOINTMENT
from patients.models import Appointment
from datetime import time, datetime, timedelta
from patients.serializers import AppointmentSerializer
#APPOINTMENT BOOKING
from rest_framework.authentication import TokenAuthentication
class AppointmentCreateView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer_instance=AppointmentSerializer(data=request.data)
        if serializer_instance.is_valid():
            #TOKEN NUMBER
            data=serializer_instance.validated_data
            d=data['doctor']#fetches doctor from client data
            date=data['appointment_date']#2026-11-04
            token=0
            appointment_time=time(9,0) #9am
            a=Appointment.objects.filter(doctor=d,appointment_date=date).last()#find the last record
            if a:
                token = (a.token_number or 0) + 1
                appointment_time=(datetime.combine(date,a.appointment_time)+timedelta(minutes=15)).time()
            else:
                token=1
            #appointment time
            serializer_instance.save(token_number=token,appointment_time=appointment_time)
            response={
                "status":"booked",
                "booking_data":serializer_instance.data
            }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


#APIVIEW FOR CREATING A USER
class PatientRegister(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

#MODEL
#SEIRALIZER
# VIEW
#PATH
# from rest_framework.authtoken.models import Token
# class Obtain_auth_token(APIView):
#     def post(self, request):
#
#         # fetches username and password from user data
#         u=request.data['username']
#         p=request.data['password']
#
#         # checks whether matching user exists in User table
#         user=authenticate(username=u,password=p)
#         #authenticate () built in function checks whether
#         #user exits or not
#         #if matching user exists if returns user objects else none
#
#
#
#         # if user exists
#         if user:
#         # generates token and sends as Response
#             token,created=Token.objects.get_or_create(user=user)
#             print(token,created)
#             return Response({'token':token.key},status=status.HTTP_201_CREATED)
#
#         else:
#             return Response({"message":"INVALID CREDENTIALS,UNABLE TO LOGIN"},status=status.HTTP_400_BAD_REQUEST)
#         # sends Response as Invalid User Credentials
