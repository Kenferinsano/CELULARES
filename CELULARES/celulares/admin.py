from django.contrib import admin
from .models import Telefono

# Registrar el modelo Telefono para que aparezca en el admin
admin.site.register(Telefono)