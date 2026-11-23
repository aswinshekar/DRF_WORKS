from accounts import serializers
from app.models import Book,BookIssue
from rest_framework import  serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"
        read_only_fields=['id']


class BookIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookIssue
        fields = "__all__"
        read_only_fields = ['id','issued_date','due_date']
