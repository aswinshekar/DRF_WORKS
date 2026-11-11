import decimal
from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
from recipes.models import recipe
# Create your models here.

class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    recipe = models.ForeignKey(recipe,on_delete=models.CASCADE)
    comment=models.TextField()
    rating=models.FloatField()
    created=models.DateTimeField(auto_now_add=True)