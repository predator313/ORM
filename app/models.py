from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     user_name=models.CharField(max_length=30)
#     password=models.CharField(max_length=30)

# class Page(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
#     page_name=models.CharField(max_length=50)
#     page_catalog=models.CharField(max_length=50)
#     publication_date=models.DateField()


#lets use the protected concept in orm 
#if there is any reference then the entity is not 
#deleted
class Page(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT,primary_key=True)
    page_name=models.CharField(max_length=30)
    page_catalog=models.CharField(max_length=50)
    publication_date=models.DateField()
