from django.shortcuts import render, redirect
from .models import *
from .forms import *

# LAS VIEWS NOS VAN A RENDERIZAR LA PAGINA

def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def quienessomos(request):
    return render(request, 'core/quienessomos.html')

def empleados(request):
    listaEmpleados = Empleado.objects.all()
    datos = { 'listaEmpleados': listaEmpleados }

    return render(request, 'core/empleados/empleados.html', datos)

def addEmpleado(request):
    datos = { 'form': EmpleadoForm() }
    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['msj'] = "Empleado guardado correctamente"

    return render(request, 'core/empleados/add.html', datos)

def updateempleado(request, id):
    empleado = Empleado.objects.get(id=id)
    datos = { 'form': EmpleadoForm(instance=empleado) }
    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST,instance=empleado, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['msj'] = "Empleado guardado correctamente"
            datos['form'] = formulario

    return render(request, 'core/empleados/update.html', datos)

def deleteempleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to='empleados')