from django.contrib import admin
from .models import Residente, Rol, UnidadHabitacional, ComplejoHabitacional

@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('tipo',)
    search_fields = ('tipo',)

@admin.register(UnidadHabitacional)
class UnidadHabitacionalAdmin(admin.ModelAdmin):
    list_display = ('numero', 'letra', 'bloque', 'piso', 'tipo')
    list_filter = ('tipo','piso')
    search_fields = ('numero', 'letra' ,'bloque')

    fieldsets = (
        (None, {
            'fields': ('numero', 'letra', 'bloque', 'piso', 'tipo')
        }),
    )

@admin.register(Residente)
class ResidenteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'correo', 'fecha_registro', 'rol', 'unidad')
    search_fields = ('rut', 'nombre', 'correo')
    list_filter = ('rol',)
    autocomplete_fields = ('rol', 'unidad')

@admin.register(ComplejoHabitacional)
class ComplejoHabitacionalAdmin(admin.ModelAdmin):
    list_display = ('nombre','direccion','tipo')
    list_filter = ('tipo',)
    search_fields = ('nombre','direccion')