from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender_choices=(('male',"MALE"),("female","FEMALE"))
    gender=models.CharField(choices=gender_choices)
    place=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    mark=models.IntegerField()
