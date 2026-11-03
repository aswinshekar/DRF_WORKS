from django.db.models import Model
from rest_framework import serializers
from django.db import models
from app.models import Movie
# from django.contrib.auth.models import User
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields = ['title', 'director', 'language', 'year', 'runtime', 'rating','image']



from django.core.mail import send_mail
from app.models import CustomUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = ['username','password','email','first_name','last_name','phone','address']
    def create(self,validated_data):#TO ENCRYPT
            # THE PASSWORD AND IT IS ALSO CALLED PASSWORD HASHING
        u=CustomUser.objects.create_user(**validated_data)
            # FOR CREATING A SUPER_USER ACCOUNT
            # User.objects.create_superuser(**validated_data)
            # ATOMATICALLY IT WILL CREATE USER AS ADMIN
        u.save()
        send_mail(
            subject="welcome to our app",
            message="thank you for signing",
            from_email="mail4aswinsekhar@gmail.com",
            recipient_list=[u.email,],
            fail_silently=True
            )
        return u

