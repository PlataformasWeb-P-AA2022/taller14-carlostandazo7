from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Propietario, Departamento

class PropietarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'edad', 'nacionalidad')
    search_fields = ('nombre', 'apellido')

admin.site.register(Propietario, PropietarioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('costo', 'nroCuartos', 'nroBaños', 'valorAlicuota', 'propietario')

    raw_id_fields = ('propietario',)

admin.site.register(Departamento, DepartamentoAdmin)
