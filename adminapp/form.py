from django.forms import ModelForm
from django import forms
from adminapp.models import dataguru, datamurid,paket

class FormGuru(ModelForm):
    class Meta:
        model = dataguru
        fields ="__all__"

class FormMurid(ModelForm):
    class Meta:
        model = datamurid
        fields ="__all__"

