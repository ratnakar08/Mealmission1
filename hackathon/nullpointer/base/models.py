from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.CharField(max_length=100)
    def __str__(self):
        return self.user.first_name
    

class food(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    dia = models.BooleanField(default=False)
    def __str__(self):
        return self.name


