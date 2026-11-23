from django.dispatch import receiver
from django.db.models.signals import post_save

from app.models import BookIssue
from datetime import timedelta


@receiver(post_save,sender=BookIssue)
def handle__bookissue_created(sender,instance,created,**kwargs):
    if created:
    #due date calculate
        instance.due_date=instance.issued_date+timedelta(days=14)
        instance.save(update_fields=['due_date'])
    #reduce available copies
        book=instance.book
        book.available_copies-=1
        book.save(update_fields=['available_copies'])

