from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=30)
    available_copies=models.IntegerField()
    def __str__(self):#returns  the string repesentation of book object
        return self.title

class BookIssue(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    student_name=models.CharField(max_length=30)
    issued_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(null=True,blank=True)
    def __str__(self):#returns  the string repesentation of bookissue object
        return self.student_name