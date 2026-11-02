from django.db import models

# from app import serializers


# Create your models here.
class Employee(models.Model):
    Gender_choices = (('male', 'MALE'), ('female', 'FEMALE'))#CHOICES=(('DBVALUES','DISPLAYVALUES')
    Name = models.CharField(max_length=30)
    #Emp_id=models.IntegerField()
    Age = models.IntegerField()
    Place=models.CharField(max_length=30)
    Gender=models.CharField(choices=Gender_choices)
    Joining_date=models.DateField(auto_now_add=True)
    Salary=models.IntegerField()
    Designation=models.CharField(max_length=30)
    image=models.ImageField(upload_to="employee",null=True,blank=True)




