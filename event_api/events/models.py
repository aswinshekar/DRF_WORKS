from django.db import models

from accounts.models import CustomUser


# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    date=models.DateField()  #yyyy/mm/dd
    time=models.TimeField() #hh.mm.ss
    venue=models.CharField(max_length=30)
    created=models.DateTimeField(auto_now_add=True)
    organizer_id=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    amount=models.IntegerField()
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    image=models.ImageField(upload_to='event',null=True,blank=True)