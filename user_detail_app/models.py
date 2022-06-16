import email
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_details(models.Model):
   email = models.EmailField(max_length=500,)
   subscribe_status= models.BooleanField(default=False)

   def __str__(self):
       return f"{self.email}"

class players(models.Model):
   name= models.CharField(max_length=1024,unique=True)
   status= models.BooleanField(default=False)

   def __str__(self):
       return f"{self.name}"
    
class player_choices(models.Model):
   email= models.ForeignKey(user_details,on_delete=models.CASCADE)
   name= models.ForeignKey(players,on_delete=models.CASCADE)
   choice_status= models.BooleanField(default=False)
   
   class Meta:
        unique_together = ('email', 'name',)

   def __str__(self):
       return f"{self.email} - {self.name} - {self.choice_status}"
    
    
