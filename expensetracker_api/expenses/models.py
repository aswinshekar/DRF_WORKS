from tkinter.constants import CASCADE
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=30)
    amount=models.IntegerField()
    category_choices=(("food","FOOD"),("bill","BILL"),("enternainment","Enternainment"),("shopping","SHOPPING"),("others","OTHERS"))
    category=models.CharField(max_length=30,choices=category_choices)
    priority_choices=(("need","NEED"),("want","WANT"))
    payment_choices=(("upi","UPI"),("cash","CASH"))
    priority=models.CharField(max_length=30,choices=priority_choices)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)#when ever updation it adds
    payment_method=models.CharField(max_length=30,choices=payment_choices)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.email
