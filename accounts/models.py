from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
class Profile(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    # name=models.CharField(max_length=100,blank=True)
    about=models.CharField(max_length=550,blank=True)
    Phone=models.IntegerField(blank=True)
    email=models.EmailField(max_length=50)
    gender=models.CharField(max_length=100,blank=True)



    def __str__(self):
      return  self.user.username



