from app import serializers

from app.models import Doctor,Appointment
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"

from django.contrib.auth.models import User
from django.db.models import Model


class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        u=User.objects.create_superuser(**validated_data)
        # u.save()
        return u

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
        read_only_fields=['id','token_number','appoinment_time','created_at']





