from django.shortcuts import render, redirect
from acounts.models import UserProfileInfo
from adminapp.models import dataguru, datamurid,paket
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import imgform, jml_pkt_forms, satuform,duaform,tigaform,empatform
from django.db.models import Q
from django.views.generic import TemplateView 
# Create your views here.

def profil(request):
    usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
    idx = usr.id
    profild = dataguru.objects.filter(no_id=idx).first()
    pakt2= paket.objects.filter(id_pkt=idx)
    return render(request, 'vcustomer/profil2.html',{ 
        'pk2':pakt2,
        'profil' : profild,
    })

def chome(request):
    if request.user.is_authenticated:
        #x=UserProfileInfo.objects.aggregate(Max('nodata'))
        #y=x.objects.annotate(diff=F(x) + F(1))

        usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
        dtgr = dataguru.objects.all()
        dtms = datamurid.objects.all()
        idx = usr.id
        foto = dataguru.objects.filter(no_id=idx).first()
        tmp = 0
        for p in dtgr:
            if p.no_id==idx:
                tmp += 1
        tmp2 = 0 
        for z in dtms:
            if z.No_id==idx:
                tmp2 += 1
        data = {
            'im' : foto,
            'usrx':usr,
            'data':dtgr,#data
            'temp':tmp,
            'temp2':tmp2,
            # 'cstm':priv,#custom
            # 'test': x
            # 'testy': y
        }
        return render(request, 'vcustomer/index.html',data)

def profilgr(request,id):
    usr  = UserProfileInfo.objects.filter(user=request.user.id).first()
    idx = usr.id
    task = dataguru.objects.filter(pk=id).first()
    x=task.no_id
    pakt= paket.objects.filter(id_pkt=x)
    dtl={
        'pk':pakt,
        'list' : task,
        'idusr':idx,
        'xd':x,
    
    }
    return render(request, 'vcustomer/profil.html',dtl)

def form(request,no):
    x=no
    # if request.method == 'POST': 
    #     iform = imgform(data=request.POST)
    #     if iform.is_valid():
    #         # file is saved
    #         iform.save()
    if request.POST:
        dataguru.objects.create(
         nama=request.POST['nama'],
         alamat=request.POST['alamat'],
         biaya=request.POST['biaya'],
         gender=request.POST['gender'],
         no_id=x,
         nohp=request.POST['nohp'],
         usia=request.POST['usia'],
         catatan=request.POST['catatan'],
         link=request.POST['link'],
         foto=request.FILES['image'],
         portofolio=request.FILES['document']
         )
        
        return redirect('chome')
    uy = dataguru.objects.all()
    return render(request,'vcustomer/form.html',{ 
        'd' : uy,
        # 'iform':iform,
        })

def guru(request):
    return render(request, 'vcustomer/guru.html')

def formklien(request,no):
    
    # if request.method == 'POST': 
    #     iform = imgform(data=request.POST)
    #     if iform.is_valid():
    #         # file is saved
    #         iform.save()
    if request.POST:
        datamurid.objects.create(
         nama=request.POST['nama'],
         alamat=request.POST['alamat'],
         No_id=no,
         nohp=request.POST['nohp'],
         gender=request.POST['gender'],

         )
        
        return redirect('chome')
    ey = dataguru.objects.all()
    return render(request,'vcustomer/formklien.html',{ 
        'e' : ey,
        # 'iform':iform,
        })

def addpaket(request):
    registered = False
    usr=UserProfileInfo.objects.filter(user=request.user.id).first()
    userid=usr.id
    template = 'vcustomer/paketform.html'
    xt=0
    
    if request.method == 'POST':
        pkts = jml_pkt_forms(data=request.POST)
        if pkts.is_valid():
            pkt = pkts.save()
            pkt.id_pkt = userid
            pkt.no_pkt = pkt.id
            xt=pkt.no_pkt
            pkt.save()
            registered = True
        else:
            print(pkts.errors)
    else:
        pkts = jml_pkt_forms()

    pack=paket.objects.filter(id=xt).first()
    pket = {
        'pct':pack,
        'pkts':pkts,
        'xt':xt,
        'registered':registered,
       }
    return render(request,template,pket)

def addhari(request,no_pkt):
    registered = False
    gtpaket=paket.objects.get(no_pkt=no_pkt)
    jml=gtpaket.jml_pertemuan
    template = 'vcustomer/paketformhari.html'
    if request.POST:
        if jml == '1X Pertemuan':
            hr=satuform(request.POST, instance=gtpaket)
            if hr.is_valid():
                hari = hr.save()
                hari.save()
                registered = True
                return redirect('profilcustomer')
            else:
                print(hr.errors)
        if jml == '2X Pertemuan':
            hr=duaform(request.POST, instance=gtpaket)
            if hr.is_valid():
                hari = hr.save()
                hari.save()
                registered = True
                return redirect('profilcustomer')
            else:
                print(hr.errors)
        if jml == '3X Pertemuan':
            hr=tigaform(request.POST, instance=gtpaket)
            if hr.is_valid():
                hari = hr.save()
                hari.save()
                registered = True
                return redirect('profilcustomer')
            else:
                print(hr.errors)
        if jml == '4X Pertemuan':
            hr=empatform(request.POST, instance=gtpaket)
            if hr.is_valid():
                hari = hr.save()
                hari.save()
                registered = True
                return redirect('profilcustomer')
            else:
                print(hr.errors)
        
    else:
        if jml == '1X Pertemuan':
            hr = satuform(instance=gtpaket)
        elif jml == '2X Pertemuan':
            hr = duaform(instance=gtpaket)
        elif jml == '3X Pertemuan':
            hr = tigaform(instance=gtpaket)
        else:
            hr = empatform(instance=gtpaket)
    sethr = {
        'hr':hr,
        'gtpaket':gtpaket,
       }
    return render(request,template,sethr)

def delpaket(request, no_pkt):
    delete_d = paket.objects.filter(no_pkt=no_pkt).delete()
    return redirect('profilcustomer')

class Cari(TemplateView):
    template_name = 'vcustomer/search2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lw = self.request.GET.get('katakunci')
        resulth = dataguru.objects.filter(
            Q(nama__contains=lw) |
            Q(catatan__contains=lw)
            )
        print(resulth)
        context = {
            "resulth":resulth,
        }
        return context