from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .models import ProduccionDiaria, Producto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProduccionDiariaForm

def index(request):
    return render(request,'core/index.html')



@login_required
def home_view(request):
    return render(request, 'core/base.html')

  
def iniciarsesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/index')
        else:
            return render(request, 'core/index.html')
    else:
        return render(request, 'core/iniciarsesion.html')
    
@login_required 
def logout_view(request):
        logout(request)
        return redirect('/iniciarsesion')

def nuevo_proyecto(request):
    return render(request, 'core/nuevo_proyecto.html')



def Ingresar_produccion(request):
        if(request.POST):
            Producto_id= request.POST['producto']
            LitrosProducidos= request.POST['litros_producidos']
            Fecha=request.POST['fecha_produccion']
            Turno=request.POST['turno']  
            Operador=request.POST['operador']

            mensaje=ProduccionDiaria()
            mensaje.producto=Producto_id
            mensaje.litros=LitrosProducidos
            mensaje.fecha=Fecha
            mensaje.turno=Turno
            mensaje.operador=Operador

            mensaje.save()
            Producto_id = Producto.objects.all() 

        return render(request,'core/nuevo_proyecto.html')