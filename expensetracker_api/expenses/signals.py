from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete


from expenses.models import Expense

@receiver(post_save,sender=Expense)
def fun(sender,instance,created,**kwargs): #created flag only in post_save
    print("HELLO")

#SENDER=SOURCE MODEL THAT SENDS NOTIFICATION/SIGNAL

#RECEIVER -A FUN THAT EXECUTES AFTR NOTIFICATION FROM SENDER

#INSTANCE= MODEL OBJECT

#@RECEIVER - DECORATOR USED TO CONNECT SENDER AND RECIEVER

@receiver(post_delete,sender=Expense)
def fun(sender,instance,**kwargs): #created flag only in post_save
    print("deleted")