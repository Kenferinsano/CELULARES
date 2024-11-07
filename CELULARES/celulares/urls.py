from django.urls import path
from . import views

urlpatterns = [
    #eich em ti el
    path('', views.index, name='index'),
    path('telefono/<int:telefono_id>/', views.telefono_detail, name='telefono_detail'),

    # jason
    path('telefonos/', views.obtener_telefonos, name='obtener_telefonos'), 
    path('telefono/<int:telefono_id>/', views.obtener_telefono, name='obtener_telefono'),
    path('agregar_telefono/', views.agregar_telefono, name='agregar_telefono'),
]
