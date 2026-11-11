from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from reviews.serializer import ReviewSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class ReivewCreate(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print(request.user)
        u=request.user#current user object
        serializer_instance=ReviewSerializer(data=request.data)#recipe,rating,comment
        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response (serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors)
from reviews.models import Review
class ReviewList(APIView):
    def get(self,request):
        r=Review.objects.all()
        serializer_instance=ReviewSerializer(r,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class ReviewRead(APIView):
    def get(self,request,i):
        # r=get_object_or_404(Review,id=i)
        r=Review.objects.filter(recipe__id=i)
        serializer_instance=ReviewSerializer(r,many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK )

class ReviewUpdate(APIView):
    def put(self,request,i):
        u = request.user
        r = get_object_or_404(Review, id=i)
        serializer_instance=ReviewSerializer(instance=r,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors)


class ReviewPartialUpdate(APIView):
    def patch(self, request, i):
        r = get_object_or_404(Review, id=i)
        u=request.user
        serializer_instance = ReviewSerializer(instance=r, data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors)

class ReviewDelete(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def patch(self, request, i):
        r = get_object_or_404(Review, id=i)
        r.delete()
        return Response({"message":"DELETED"})






