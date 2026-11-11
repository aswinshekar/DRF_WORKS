"""
URL configuration for recipe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from recipes import views

urlpatterns = [
    path('list/',views.RecipeList.as_view()),
    path('view/<int:i>',views.RecipeView.as_view()),
    path('create/',views.RecipeCreate.as_view()),
    path('update/<int:i>',views.RecipeUpdate.as_view()),
    path('partialupdate/<int:i>',views.RecipePartialUpdate.as_view()),
    path('delete/<int:i>',views.RecipeDelete.as_view())
]
