from django.shortcuts import render

# Create your views here.

def base(request):
    context={}
    return render(request, 'web/base.html', context)

def inicio(request):
    context={}
    return render(request, 'web/inicio.html', context)

def nosotros(request):
    return render(request, 'web/nosotros.html') 

def galeria(request):
    return render(request, 'web/galeria.html')


# FUNCIONES LOGIN

def login(request):
    return render(request, 'registration/login.html')