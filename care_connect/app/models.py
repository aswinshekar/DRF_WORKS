from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=30)
    SPECIALIZATION_OPTIONS = (
        ("cardiology", "Cardiology"),
        ("dermatology", "Dermatology"),
        ("endocrinology", "Endocrinology"),
        ("ent", "Ear, Nose & Throat (ENT)"),
        ("gastroenterology", "Gastroenterology"),
        ("general_medicine", "General Medicine / Internal Medicine"),
        ("general_surgery", "General Surgery"),
        ("gynecology", "Gynecology & Obstetrics"),
        ("hematology", "Hematology"),
        ("nephrology", "Nephrology"),
        ("neurology", "Neurology"),
        ("oncology", "Oncology"),
        ("ophthalmology", "Ophthalmology"),
        ("orthopedics", "Orthopedics"),
        ("pediatrics", "Pediatrics"),
        ("psychiatry", "Psychiatry"),
        ("pulmonology", "Pulmonology"),
        ("radiology", "Radiology"),
        ("urology", "Urology"),
        ("other", "Other"),
    )
    specialization=models.CharField(choices=SPECIALIZATION_OPTIONS)
    fee=models.IntegerField(null=True)
    qualification=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
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