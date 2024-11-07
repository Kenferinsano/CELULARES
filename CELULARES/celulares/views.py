from django.shortcuts import render
from django.http import HttpResponse
from .models import Telefono
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Para evitar problemas con CSRF en Postman
import json

#----------------------- VISTAS BASICAS PARA HTML ----------------------

def index(request):
    telefonos = Telefono.objects.all()
    response = "<h1>Lista de Teléfonos</h1><ul>"

    for telefono in telefonos:
        response += f"<li><a href='/telefono/{telefono.id}/'>{telefono.nombre}</a></li>"

    response += "</ul>"
    if not telefonos:
        response += "<p>No hay teléfonos disponibles.</p>"

    return HttpResponse(response)

def telefono_detail(request, telefono_id):
    telefono = get_object_or_404(Telefono, id=telefono_id)
    
    response = f"""
    <h1>{telefono.nombre}</h1>
    <p><strong>Marca:</strong> {telefono.marca}</p>
    <p><strong>Precio:</strong> ${telefono.precio}</p>
    <p><strong>Descripción:</strong> {telefono.descripcion}</p>
    <br>
    <a href="/">Volver a la lista</a>
    """

    return HttpResponse(response)


#------------------------- GET POR POSTMAN ----------------------

def obtener_telefonos(request):
    telefonos = Telefono.objects.all()

    telefonos_list = [
        {
            'id': telefono.id,
            'nombre': telefono.nombre,
            'marca': telefono.marca,
            'precio': telefono.precio,
            'descripcion': telefono.descripcion
        }
        for telefono in telefonos
    ]

    return JsonResponse(telefonos_list, safe=False) 

#Se obtiene el celular por id :DD

def obtener_telefono(request, telefono_id):
    telefono = get_object_or_404(Telefono, id=telefono_id)

    telefono_data = {
        'id': telefono.id,
        'nombre': telefono.nombre,
        'marca': telefono.marca,
        'precio': telefono.precio,
        'descripcion': telefono.descripcion
    }

    return JsonResponse(telefono_data)

#------------------------- POST POR POSTMAN ----------------------


@csrf_exempt 
def agregar_telefono(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            nombre = data.get('nombre')
            marca = data.get('marca')
            precio = data.get('precio')
            descripcion = data.get('descripcion')

            if not nombre or not marca or not precio or not descripcion:
                return JsonResponse({'error': 'Todos los campos son requeridos.'}, status=400)

            telefono = Telefono.objects.create(
                nombre=nombre,
                marca=marca,
                precio=precio,
                descripcion=descripcion
            )

            return JsonResponse({'message': 'Teléfono agregado exitosamente!', 'id': telefono.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos inválidos o malformateados en el cuerpo de la solicitud.'}, status=400)



