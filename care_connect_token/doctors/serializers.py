# from DATE_TIME_MODULE import todays_date
from doctors.models import Doctor
from rest_framework import serializers
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"

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
