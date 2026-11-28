# from urllib import request
#
# from django.db.models.query_utils import Q
# from django.shortcuts import render, get_object_or_404
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
#
# from recipes.models import recipe
# from reviews.permissions import IsOwner
# from reviews.serializer import ReviewSerializer
# from rest_framework import status
# from rest_framework.response import Response
#
# # Create your views here.
# class ReivewCreate(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def post(self,request):
#         print(request.user)
#         u=request.user#current user object
#         serializer_instance=ReviewSerializer(data=request.data)#recipe,rating,comment
#         if serializer_instance.is_valid():
#             serializer_instance.save(user=u)
#             return Response (serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors)
# from reviews.models import Review
# class ReviewList(APIView):
#     def get(self,request):
#         r=Review.objects.all()
#         serializer_instance=ReviewSerializer(r,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
# class ReviewRead(APIView):
#     def get(self,request,i):
#         # r=get_object_or_404(Review,id=i)
#         r=Review.objects.filter(recipe__id=i)
#         serializer_instance=ReviewSerializer(r,many=True)
#         return Response(serializer_instance.data, status=status.HTTP_200_OK )
#
# class ReviewUpdate(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated,IsOwner]
#     def put(self,request,i):
#         # u = request.user
#         r = get_object_or_404(Review, id=i)
#         self.check_object_permissions(request,r)#manually checks if requested user has permissions
#         #to perform the following operations on review object r
#         serializer_instance=ReviewSerializer(instance=r,data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors)
#
# class ReviewPartialUpdate(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated,IsOwner]
#     def patch(self, request, i):
#         r = get_object_or_404(Review, id=i)
#         self.check_object_permissions(request,r)
#         serializer_instance = ReviewSerializer(instance=r, data=request.data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors)
#
# class ReviewDelete(APIView):
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def patch(self, request, i):
#         r = get_object_or_404(Review, id=i)
#         r.delete()
#         return Response({"message":"DELETED"})
#
# from django.db.models import Q
# from recipes.serializers import recipeserializer
# class ReviewSearch(APIView):
#     def get(self,request):
#         #fetches keywords from query parameters
#         data=request.query_params.get('search')
#         #reads all records matching with the keyword from db table(using filter)
#         m=recipe.objects.filter((Q(recipe_name__icontains=data))|
#                                 Q(ingredients__icontains=data ))
#         serializer_instance=recipeserializer(m,many=True)
#
#         return Response(serializer_instance.data)
#
#
#
