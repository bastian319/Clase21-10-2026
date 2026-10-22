from django.contrib import admin

# Register your models here.
from .models import Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    list_display = ('id','nombre','apellido','sueldo')

    search_fields = ('nombre','apellido',)

    ordering = ('apellido','nombre',)