# from django.shortcuts import render, get_object_or_404
# from django.views import View
# from django.http import JsonResponse
# from app import serializers
# from app.models import Employee
# # Create your views here.
# #API VIEW FOR READINFG ALL RECORD
# #using django
# # class EmployeeList(View):
# #     def get(self, request):
# #         s=list(Employee.objects.all().values())
# #         return JsonResponse(s, safe=False)
# #using DRF
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from app.serializers import EmployeeSerializer
# # class EmployeeList(APIView):
# #     def get(selfself,request):
# #         #reads all employee records
# #         qs=Employee.objects.all() #DJANGO FORMAT QS
# #         # CONVERTS QUERYSET INTO PYTHON NATIVE USING SERIALIZER
# #         serializer_instance=EmployeeSerializer(qs,many=True)
# #         # RETURNS RESPONSE AS JSON USING RESPONSE FUNTION
# #         # print(serializer_instance.data)
# #         return Response(serializer_instance.data)
#
# # using mixing
# from rest_framework import mixins,generics
# # class EmployeeList(mixins.ListModelMixin,generics.GenericAPIView):
# #     queryset=Employee.objects.all()
# #     serializer_class= serializers.EmployeeSerializer
# #     def get(self,request):
# #         return self.list(request)
# #USING GENERIC
# class EmployeeList(generics.ListAPIView):
#     queryset=Employee.objects.all()
#     serializer_class= serializers.EmployeeSerializer
#
# # #API VIEW FOR READING A SPECIFIC RECORD
# #USING DJANGO
# # class EmployeeDetail(View):
# #     def get(self, request,i):
# #         #reads data from employee table matching with id i
# #         s=Employee.objects.filter(id=i)
# #         #converts the data into python native type
# #         data=list(s.values())
# #         #return response
# #         return JsonResponse(data,safe=False)
# #using DRF
# # class EmployeeDetail(APIView):
# #     def get(self,request,i):
# #         #reads employee record matching id
# #         # e=Employee.objects.get(id=i)
# #         e=get_object_or_404(Employee,id=i)
# #         #calls employee serializer class for serialization\
# #         serializer_instance=EmployeeSerializer(e)
# #         #sends response back to client
# #         return Response(serializer_instance.data)
# # USING MIXING
# # class EmployeeDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
# #     queryset = Employee.objects.all()
# #     serializer_class = serializers.EmployeeSerializer
# #     def post(self, request,pk):
# #         return self.retrieve(request,pk)
# #USING GENERIC
# class EmployeeDetail(generics.RetrieveAPIView):
#     queryset=Employee.objects.all()
#     serializer_class= serializers.EmployeeSerializer
#
# #API VIEW FOR CREATING A NEW RECORD
# # USING DJANGO
# # from json import loads
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # @method_decorator(csrf_exempt,name="dispatch")
# #
# # class EmployeeCreate(View):
# #     def post(self,request):
# #         #fetches the data from client side
# #         form_data=request.body
# #         #converts json data into python native type
# #         data=loads(form_data)
# #         n = data['Name']
# #         a = data['Age']
# #         p = data['Place']
# #         g = data['Gender']
# #         s = data['Salary']
# #         d = data['Designation']
# #         # employee = Employee.objects.create(**data)
# #         # creates a new record inside db table
# #         s=Employee.objects.create(Name=n, Age=a, Place=p, Gender=g, Salary=s, Designation=d)
# #         s.save()
# #         #returns response
# #         return JsonResponse({'messgae':"created"})
# # #using DRF
# # class EmployeeCreate(APIView):
# #     def post(self,request):
# #         data=request.data#PYTHON NATIVE TYPE
# #         # VALIDATION+CONVERSION(NATIVE TO MODEL OBJECT)
# #         serializer_instance = EmployeeSerializer(data=request.data)
# #         print(request.data)
# #
# #         # CHECKS WHERETHER THE DATA COMING FROM CLIENT IS VALID,IF VALID
# #         # SAVES THE DATA INTO MODEL
# #         #
# #         if serializer_instance.is_valid():
# #             serializer_instance.save()#SAVES THE DATA  INTO MODEL
# #             return Response(serializer_instance.data)# SENDS CREATED OBJECT AS RESPONSE
# #        # IF DATA IS NOT VALID IT WILL SHOW VALIDATION ERRORS
# #
# #         else:
# #             return Response(serializer_instance.errors)
# #USINF MIXIN CLASS
#
# class EmployeeCreate(mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = serializers.EmployeeSerializer
#     def post(self, request):
#         return self.create(request)
#
# # #API VIEW FOR DELETING RECORD
# # USING DJANGO
# # @method_decorator(csrf_exempt,name="dispatch")
# # class EmployeeDelete(View):
# #     def delete(self,request,i):
# #         #fetch the data from students table matching id i
# #         s=Employee.objects.get(id=i)
# #         #DELETE THE RECORD
# #         s.delete()
# #         #RETURNS RESPONSE BACK TO CLIENT
# #         return JsonResponse({"message":"deleted"})
# #using DRF
#
# class EmployeeDelete(APIView):
#     def delete(self,request,i):
#         #read record mathcing with id
#         e=get_object_or_404(Employee,id=i)
#         e.delete()
#         return Response("message : DELETED RECORD SUCCEFULLY ")
#
# #
# # #API TO UPDATE A EXISTING RECORD
# # USING DJANGO
# # from json import loads
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # @method_decorator(csrf_exempt,name="dispatch")
# # class EmployeeUpdate(View):
# #     def put(self,request,i):
# #         # FETCH THE DATA FROM CLIENT SIDE
# #         form_data = request.body
# #         #CONVERTS THE DATA INTO NATIVE
# #         data = loads(form_data)
# #
# #         # READS THE RECORD MATCHING WITH ID FROM DB TABLE
# #         s = Employee.objects.get(id=i)
# #         # UPDATE THE RECORD
# #         s.Name = data['Name']
# #         s.Age = data['Age']
# #         s.Place = data['Place']
# #         s.Gender = data['Gender']
# #         s.Salary = data['Salary']
# #         s.Designation = data['Designation']
# #         #SAVES THE RECORD
# #         s.save()
# #         # RETURNS RESPONSE BACK TO CLIENT
# #         return JsonResponse({'message':'UPDATED'})
# #
#
#
# #using DRF
#
# class EmployeeUpdate(APIView):
#     def put(self,requst,i):
#         #READS THE RECORD MATCHING WITH ID
#         e=get_object_or_404(Employee,id=i)
#         #FETCHES THE DATA COMING FROM CLIENT
#         data=requst.data
#         #CALLS EMPLOYEE SERIALIZER CLASS FOR DESERIALIZATION
#         serializer_instance =EmployeeSerializer(instance=e,data=data)
#         if serializer_instance.is_valid():
#                 #SAVE THE RECORD
#                 serializer_instance.save()
#         #SENDS RESPONSE BACK TO CLIENT
#                 return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#
#
#
#
# # #API TO UPDATE DATA PARTIALY (patch)
# # USING DJANGO
# # from json import loads
# # from django.views.decorators.csrf import csrf_exempt
# # from django.utils.decorators import method_decorator
# # @method_decorator(csrf_exempt,name="dispatch")
# # class EmployeePartialUpdate(View):
# #     def patch(self,request,i):
# #         # FETCH THE DATA FROM CLIENT SIDE
# #         form_data = request.body
# #         # CONVERTS THE DATA INTO NATIVE
# #         data = loads(form_data)
# #         print(data)
# #         # READS THE RECORD MATCHING WITH ID FROM DB TABLE
# #         s = Employee.objects.get(id=i)
# #         # UPDATE THE RECORD
# #         if 'Name' in data:
# #             s.Name = data['Name']
# #         if 'Age' in data:
# #             s.Age = data['Age']
# #         if 'Place' in data:
# #             s.Place = data['Place']
# #         if 'Gender' in data:
# #             s.Gender = data['Gender']
# #         if 'Salary' in data:
# #             s.Salary = data['Salary']
# #         if 'Designation' in data:
# #             s.Designation = data['Designation']
# #         # SAVES THE RECORD
# #         s.save()
# #         # RETURNS RESPONSE BACK TO CLIENT
# #         return JsonResponse({'message': 'UPDATED'})
# #using DRF
#
#
# class EmployeePartialUpdate(APIView):
#     def patch(self,requst,i):
#         #READS THE RECORD MATCHING WITH ID
#         e=get_object_or_404(Employee,id=i)
#         #FETCHES THE DATA COMING FROM CLIENT
#         data=requst.data
#         #CALLS EMPLOYEE SERIALIZER CLASS FOR DESERIALIZATION
#         serializer_instance =EmployeeSerializer(instance=e,data=data,partial=True)
#         if serializer_instance.is_valid():
#                 #SAVE THE RECORD
#                 serializer_instance.save()
#         #SENDS RESPONSE BACK TO CLIENT
#                 return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
from rest_framework import viewsets
from app.models import Employee
from app.serializers import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):#GET/POST/PUPATCH/DELETE#
     queryset=Employee.objects.all()
     serializer_class=EmployeeSerializer
