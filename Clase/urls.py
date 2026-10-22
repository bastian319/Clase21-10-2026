from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
urlpatterns = [
    path('',views.lista_empleados, name='lista_empleados',name='lista_empleados'),
    path('empleado/<int:pk>/',views.detalle_empleado,name='detalle_empleado'),
    path('crear/',views.crear_empleado,name='crear_empleado'),
    path('editar/<int:pk>/',views.editar_empleado,name='editar_empleado'),
    path('eliminar/<int:pk>/',views.eliminar_empleado,name='eliminar_empleado'),
    path('login/',auth_views.LoginView.as_view(template_name='empleados/login.html'),name='login'),
    path('logout/',auth_views.LoginView.as_view(),name='logout'),
]