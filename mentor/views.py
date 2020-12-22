from django.shortcuts import render

# Create your views here.

def mhome(request):
    return render(request 'vmentor/index.html')

def mdetail(request):
    return render(request 'vmentor/detail.html')