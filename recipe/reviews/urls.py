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
from reviews import views

urlpatterns = [
    path('review',views.ReivewCreate.as_view()),
    path('list',views.ReviewList.as_view()),
    path('review_read/<int:i>',views.ReviewRead.as_view()),
    path('update/<int:i>',views.ReviewUpdate.as_view()),
    path('pupdate/<int:i>',views.ReviewPartialUpdate.as_view()),
    path('delete/<int:i>',views.ReviewDelete.as_view()),
    path('search',views.ReviewSearch.as_view())

]
