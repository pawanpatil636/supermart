from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES=(
   ('male','male'), 
   ('female','female'),
   ('others','others'),
)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    mobile_number = models.CharField(max_length=10) 
    DOB = models.DateField()
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES)
    age =models.IntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)
