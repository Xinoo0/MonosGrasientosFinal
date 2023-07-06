from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto


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

# FUNCIONES CRUD

def crud(request):
    pro=Producto.objects.all()
    return render(request,'web/crud.html',{'pro':pro})

def agregar(request):
    return render(request,'web/agregar.html')

def agregarrec(request):
    w=request.POST['nombre']
    x=request.POST['modelo']
    y=request.POST['marca']
    z=request.POST['precio']
    pro=Producto(nombre=w,modelo=x,marca=y,precio=z)
    pro.save()
    return redirect("/")

def eliminar(request,id):
    pro=Producto.objects.get(id=id)
    pro.delete()
    return redirect("/")

def actualizar(request,id):
    pro=Producto.objects.get(id=id)
    return render(request,'web/actualizar.html',{'pro':pro})

def actualizarrec(request,id):
    w=request.POST['nombre']
    x=request.POST['modelo']
    y=request.POST['marca']
    z=request.POST['precio']
    pro=Producto.objects.get(id=id)
    pro.nombre=w
    pro.modelo=x
    pro.marca=y
    pro.precio=z
    pro.save()
    return redirect("/")

# FUNCIONES LOGIN

def login(request):
    return render(request, 'registration/login.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('home')
    return render(request, 'registration/register.html',data)

# FUNCIONES ADMINISTRADORES

@login_required
def products(request):
    return render(request, 'web/crud.html')