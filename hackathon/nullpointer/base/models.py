from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    

class food(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    dia = models.BooleanField(default=False)
    def __str__(self):
        return self.name


