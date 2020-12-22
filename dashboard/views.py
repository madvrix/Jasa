from django.shortcuts import render
from adminapp import models
from django.db.models import Q
from django.views.generic import TemplateView 

# Create your views here.

def home(request):
    dt = models.dataguru.objects.all()
    return render(request, 'tampildashboard/index.html',{ 
        'data' : dt,
    }) 

def profildashboard(request,id):
    task = models.dataguru.objects.filter(pk=id).first()
    x=task.no_id
    pakt= models.paket.objects.filter(id_pkt=x)
    return render(request, 'tampildashboard/profil.html',{ 
        'list' : task,
        'pk':pakt,
    })

def guruf(request):
    return render(request, 'tampildashboard/guruf.html')

class SearchView(TemplateView):
    template_name = 'tampildashboard/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET.get('keyword')
        resulth = models.dataguru.objects.filter(
            Q(nama__contains=kw) |
            Q(catatan__contains=kw)
            )
        print(resulth)
        context = {
            "resulth":resulth,
        }
        return context
    