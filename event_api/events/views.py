from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView

from events.permissions import IsOrganizerOrReadOnly

from rest_framework.response import Response
from events.models import Event
from events.serializers import  EventSerializer
from rest_framework import status
# Create your views here.
class EventListCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self,request):
        qs=Event.objects.all()
        serializer_instance=EventSerializer(data=qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer_instance=EventSerializer(data=request.body)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class EventRetriveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self,request,pk):
            qs = Event.objects.filter(Event,id=pk)
            serializer_instance = EventSerializer(data=qs)
            return Response(serializer_instance.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
        pass
    def delete(self,request,pk):
        pass