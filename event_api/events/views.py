import rest_framework
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from events.permissions import IsOrganizerOrReadOnly

from rest_framework.response import Response
from events.models import Event
from events.serializers import  EventSerializer
from rest_framework import status
# Create your views here.
# class EventListCreateView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsOrganizerOrReadOnly]
#     def get(self,request):
#         if request.user.role=='customer':
#             qs=Event.objects.all()#IF CUSTOMER READS ALL RECORDS
#         else:
#             qs=Event.objects.filter(organizer=request.user)#IF ORGANIZER ONLY THERIR RECORD
#         serializer_instance=EventSerializer(qs,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#

    def post(self,request):
        serializer_instance=EventSerializer(data=request.body)
        if serializer_instance.is_valid():
            serializer_instance.save(organizer=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class EventRetriveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self, request, pk):

        if request.user.roles=='customer':
            e = get_object_or_404(Event, id=pk)
        else:
            e = get_object_or_404(Event, id=pk,organizer=request.user)
        serializer_instance = EventSerializer(e)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)



    def put(self,request,pk):
        e = get_object_or_404(Event, id=pk)
        self.check_object_permissions(request, e)
        serializer_instance = EventSerializer(instance=e, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        e = get_object_or_404(Event, id=pk)
        self.check_object_permissions(request, e)
        e.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
