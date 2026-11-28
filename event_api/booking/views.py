from django.db.migrations import serializer
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from booking.models import Booking
from booking.serializers import BookingSerializer
from rest_framework import status
from rest_framework.response import Response


# Create your views here.


class BookingListCreate(APIView):
    def post(self, request):
        serializer_instance = BookingSerializer(data=request.user)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        b = Booking.objects.all()
        serializer_instance = BookingSerializer(b, many=True)
        return Response(serializer_instance.data, status=status.HTTP_200_OK)


class BookingRetrieveUpdateDelete(APIView):
    def get(self, request, pk):
        if request.user.role == 'customer':
            b = get_object_or_404(Booking, id=pk)
        else:
            b = get_object_or_404(Booking, id=pk, organizer=request.user)

        serializer_instance = BookingSerializer(b)
        return Response(serializer_instance.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        b = get_object_or_404(Booking, id=pk)
        self.check_object_permissions(request, b)
        serilaizer_instance = BookingSerializer(instance=b, data=request.data)
        if serilaizer_instance.is_valid():
            serilaizer_instance.save()
            return Response(serilaizer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilaizer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        b = get_object_or_404(Booking, id=pk)
        self.check_object_permissions(request, b)
        b.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

