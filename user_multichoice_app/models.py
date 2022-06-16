from django.db import models

# Create your models here.

class user_info(models.Model):
   email = models.EmailField(max_length=500,unique=True)
   subscribe_status= models.BooleanField(default=False)

   def __str__(self):
       return f"{self.email}"

class player_info(models.Model):
   name= models.CharField(max_length=1024,unique=True)
   status= models.BooleanField(default=False)

   def __str__(self):
       return f"{self.name}"
    
class user_player_choice(models.Model):
   email= models.ForeignKey(user_info,on_delete=models.CASCADE)
   name = models.ManyToManyField(player_info)
   # choice_status= models.BooleanField(default=False)
   
#    class Meta:
#         unique_together = ('email', 'name',)

   def __str__(self):
       return f"{self.email}"
      #  return f"{self.email} - {self.name} - {self.choice_status}"