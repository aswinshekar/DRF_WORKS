from rest_framework import serializers
from booking.models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='_all_'
        read_only_fields=['id','user','created_at','ticket_code']