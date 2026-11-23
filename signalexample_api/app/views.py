from django.shortcuts import render
from rest_framework.views import APIView
from app.models import Book,BookIssues
from app.serializers import BookSerializer,BookIssuesSerializer

# Create your views here.


class BookListCreate(APIView):
    def get(self,request):



    def post(self,request):

class BookIssueListCreate(APIView):
    def get(self,request):
        pass
    def post(self,request):
        pass
