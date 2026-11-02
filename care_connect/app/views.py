from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
#API VIEWS FOR CREATING DOCTOR
#API VIEWS FOR READING ALL DOCTORS
class DoctorListCreateView(APIView):
    def get(self,request):
        pass
    def post(self,request):
        pass


class RetrieveUpdateDelete(APIView):
    def get(self,request,pk):
        pass
    def put(self,requst,pk):
        pass
    def delete(self,request,pk):
        pass



#API VIEWS FOR READING A SPECIFIC DOCTOR
#API VIEWS FOR UPDATING A DOCTOR
#API VIEWS FOR DELETING A DOCTOR
#API VIEWS FOR FILTERING DOCTORS BASED ON SPECIFICATIONS
class DoctorFilter(APIView):
    def get(self,request):
        pass

