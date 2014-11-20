from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    register_date = models.DateTimeField("Date Registered")
    active = models.IntegerField(default=0)

class Comments(models.Model):
    cmt_text = models.CharField(max_length=200)
    user = models.ForeignKey(Users)
    create_date= models.DateTimeField("Date Registered")
    active = models.IntegerField(default=0)
