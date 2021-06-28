from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Timeline(models.Model):
  name = models.CharField(max_length=100)

class extendedUser(models.Model):
  user = models.OneToOneField(User, on_delete=CASCADE)
  email = models.CharField(max_length=100)
  profile_pic = models.CharField(max_length=200)

  def __str__(self):
    return self.email
  

