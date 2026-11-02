from django.db.models import Model
from rest_framework import serializers
from django.db import models
from app.models import Employee
# Create your models here.
class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    Gender_choices = (('male', 'MALE'), ('female', 'FEMALE'))#CHOICES=(('DBVALUES','DISPLAYVALUES')
    Name = serializers.CharField(max_length=30)
    #Emp_id=models.IntegerField()
    Age = serializers.IntegerField()
    Place=serializers.CharField(max_length=30)
    Gender=serializers.ChoiceField(choices=Gender_choices)
    Joining_date=serializers.DateField(read_only=True)
    image=serializers.ImageField()
    Salary=serializers.IntegerField()
    Designation=serializers.CharField(max_length=30)



    # AFTER VALIDATION AND BEFORE SAVING THIS FUNCTION IS CALLED
    def create(self,validated_data):
        e=Employee.objects.create(**validated_data)
        return e
    #AFTER VALIDATION BEFORE SAVING
    def update(self,instance,validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.Name = validated_data.get('Name',instance.Name)
        instance.Age = validated_data.get(' Age',instance.Age)
        instance.Place=validated_data.get('Place',instance.Place)
        instance.Gender = validated_data.get('Gender',instance.Gender)
        instance.Joining_date= validated_data.get('Joining_date',instance.Joining_date)
        instance.Salary = validated_data.get('Salary',instance.Salary)
        instance.Designation= validated_data.get('Designation',instance.Designation)
        instance.save()
        return instance
#
# class EmployeeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Employee
#         fields ='__all__'
#         read_only_fields=['id','joining_date']
#
#     def validate(self,data):
#         if data['Age']<=0:
#             raise serializers.ValidationError("AGE SHOULD BE POSITIVE")
#           return data
#         elif data['Age']<=18:
#             raise serializers.ValidationError("AGE SHOULD BE GREATER THAN 18")










