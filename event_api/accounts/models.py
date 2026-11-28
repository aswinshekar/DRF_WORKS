# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
#
# class CustomUser(AbstractUser):
#     role_choices=(('organizer','Organizer'),
#                   ('customer','Customer'))
#     roles=models.CharField(max_length=20,choices=role_choices,default='customer')
#     phone=models.CharField(max_length=20,null=True,blank=True)
#     def __str__(self):
#         return self.username
