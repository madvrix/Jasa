from django import forms
from adminapp.models import dataguru, paket

class imgform(forms.ModelForm):
    class Meta():
         model = dataguru
         fields = ('foto',)

class jml_pkt_forms(forms.ModelForm):
    class Meta():
        model = paket
        fields =('nama_pkt','jml_pertemuan','biaya')

class satuform(forms.ModelForm):
    class Meta():
        model = paket
        fields = ('hari_1','jam_1')

class duaform(forms.ModelForm):
    class Meta():
        model = paket
        fields = ('hari_1','jam_1','hari_2','jam_2')
class tigaform(forms.ModelForm):
    class Meta:
        model = paket
        fields = ('hari_1','jam_1','hari_2','jam_2','hari_3','jam_3')
class empatform(forms.ModelForm):
    class Meta():
        model = paket
        fields = ('hari_1','jam_1','hari_2','jam_2','hari_3','jam_3','hari_4','jam_4')