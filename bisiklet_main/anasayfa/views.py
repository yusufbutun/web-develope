from django.shortcuts import render

# Create your views here.

def anasayfa(request, *args, **kwargs):
    return render(request, "anasayfa.html")

def iletisim(request, *args, **kwargs):
    return render(request, "iletisim.html")