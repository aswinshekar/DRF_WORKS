from django.db import models

# Create your models here.

class Patient(models.Model):
    gender_choices=(('male',"MALE"),('female','FEMALE'))
    patient_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=10,choices=gender_choices)
    phone=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True)
    disease=models.CharField(max_length=30)
    admission_date=models.DateField(auto_now_add=True)
    is_discharged=models.BooleanField(default=False)

