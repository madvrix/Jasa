from django import forms
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CHOICES=[('2','Vendor'),('3','Client')]

class UserProfileInfo(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, blank=True, null=True)
    nodata = models.IntegerField(null=True)
    # norole = models.IntegerField(null=True)
    norole = models.CharField(max_length=200,choices=CHOICES,null=True)
    #role=models.CharField(widget=forms.RadioSelect(choices=CHOICES))

    

    def __str__(self):
        return self.user.username