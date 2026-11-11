from patients.models import Appointment
from rest_framework import serializers
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password','email']
    def create(self,validated_data):
        u=User.objects.create_superuser(**validated_data)
        u.save()
        return u

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"
        read_only_fields=['id','token_number','appoinment_time','created_at']

    def validate(self,validated_data):
        appointment_date=validated_data['appointment_date']
        d=validated_data['doctor']
        todays_date=datetime.now().date()

        if appointment_date<todays_date:
            raise serializers.ValidationError("Invalid date")

        a=Appointment.objects.filter(doctor=d,appointment_date=appointment_date).last()
        if a:
            if a.token_number==25:
                raise serializers.ValidationError("Slots full")

        return validated_data


