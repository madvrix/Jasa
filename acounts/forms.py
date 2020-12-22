from django import forms
from .models import UserProfileInfo
from adminapp.models import datamurid
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
         model = UserProfileInfo
         fields = ('nama', 'norole',)
class datamform(forms.ModelForm):
    class Meta():
         model = datamurid
         fields = ('alamat','nohp','pendidikan')