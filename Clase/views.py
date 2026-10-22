from django.shortcuts import render
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

def es_administrador(user):
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.groups.filter(
                name='Administrador'
            ).exists()
        )
    )

def es_usuario_autorizado(user):
    return (
        user.is_authenticated
        and (
            user.is_superuser
            or user.groups.filter(
                name__in=['Administrador', 'Invitado']
            ).exists()
        )
    )

def administrador_requerido(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):

        if not es_administrador(request.user):
            raise PermissionDenied

        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
def lista_empleados(request):

    if not es_usuario_autorizado(request.user):
        raise PermissionDenied

    empleados = Empleado.objects.all()

    contexto= {
        'empleados': empleados,
        'es_administrador': es_administrador(
            request.user
        ),
    }

    return render(request,'empleados/lista.html', contexto)

@administrador_requerido
def detalle_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    return render(request,'empleados/detalle.html', {'empleado': empleado})

@administrador_requerido
def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
        else:
            form = EmpleadoForm()
        return render(request, 'empleados/crear.html', {'form':form})

@administrador_requerido
def editar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(
            request.POST,
            instance=empleado
        )
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/editar.html', {'form':form,'empleado':empleado,})

@administrador_requerido
def eliminar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('lista_empleados')

    return render(request, 'empleados/eliminar.html',{'empleado':empleado})