from django.contrib import admin
from reviews.models import Review
from recipes.models import recipe
# Register your models here.
admin.site.register(Review)
admin.site.register(recipe)