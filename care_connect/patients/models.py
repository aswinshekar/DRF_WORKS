from django.db import models
from doctors.models import Doctor
# Create your models here.
class Appointment(models.Model):
    patient_name=models.CharField(max_length=30)
    age=models.IntegerField()
    gender_choice=(("male","MALE"),("female","FEMALE"))
    gender=models.CharField(choices=gender_choice)
    phone=models.CharField(max_length=20)
    problem=models.TextField()
    appointment_date=models.DateField()# APPOINTMENT DATE
    appointment_time=models.TimeField(null=True)
    token_number=models.IntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)#DATE INN WHICH RECORD IS SAVED IN DB TABLE
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)