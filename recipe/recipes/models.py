from django.db import models

# Create your models here.
class recipe(models.Model):
    recipe_name=models.CharField(max_length=30)
    mealtype_choices=(('breakfast','BREAKFAST'),('lunch','LUNCH'),('dinner','DINNER'))
    cuisine_choices=(('indian','INDIAN'),('italian','ITALIAN'),('chinese','CHINESE'))
    ingredients=models.TextField()
    instructions=models.TextField()
    mealtype=models.CharField(max_length=30,choices=mealtype_choices)
    cuisine=models.CharField(max_length=30,choices=cuisine_choices)
    image=models.ImageField(upload_to="recipe")
    def __str__(self):
        return self.recipe_name