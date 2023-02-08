from .models import  Page
from django.db.models.signals import post_delete
from django.dispatch import receiver
#here we are going to do all signals related to work
@receiver(post_delete,sender=Page)
def delete_related_user(sender,instance,**kwargs):
    print('page post delete signal is working')
    instance.user.delete()
#now lets trigger the signal to use it
#otherwise it is nothing


