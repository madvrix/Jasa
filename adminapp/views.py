from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
from django.contrib import messages
from adminapp.form import FormGuru, FormMurid

# Create your views here.

def tampil(request):
    return render(request, 'vadmin/index.html')

def murid(request):
    return render(request, 'vadmin/murid.html')

# PENGAJAR

def tampilguru(request):
    if request.POST:
        models.dataguru.objects.all()
        
    ptampil = models.dataguru.objects.all()
    return render(request, 'vadmin/pengajar.html',
		{ 'data': ptampil,
		})

def detailguru(request, id):
	gdetail = models.dataguru.objects.filter(pk=id).first()
	return render(request, 'vadmin/detailpengajar.html',
		{ 'data': gdetail,
		})

def editguru(request, id_guru):
    juduls = models.dataguru.objects.get(id=id_guru)
    template = 'vadmin/editguru.html'
    if request.POST:
        form = FormGuru(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/tampilguru', id_guru=id_guru)
    else:
        form = FormGuru(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def deleteguru(request, id):
    delete_d = models.dataguru.objects.filter(pk=id).delete()
    return redirect('/adminapp/tampilguru')

# MURID

def tampilmurid(request):
    if request.POST:
        models.datamurid.objects.all()
        
    mtampil = models.datamurid.objects.all()
    return render(request, 'vadmin/murid.html',
		{ 'data': mtampil,
		})

def detailmurid(request, id):
	mdetail = models.datamurid.objects.filter(pk=id).first()
	return render(request, 'vadmin/detailmurid.html',
		{ 'data': mdetail,
		})

def editmurid(request, id_murid):
    juduls = models.datamurid.objects.get(id=id_murid)
    template = 'vadmin/editmurid.html'
    if request.POST:
        form = FormMurid(request.POST, instance=juduls)
        if form.is_valid():
            form.save()
            return redirect('/adminapp/tampilmurid', id_murid=id_murid)
    else:
        form = FormMurid(instance=juduls)
        konteks = {
            'form':form,
            'juduls':juduls
        }
    return render(request, template, konteks)

def deletemurid(request, id):
    delete_d = models.datamurid.objects.filter(pk=id).delete()
    return redirect('/adminapp/tampilmurid')