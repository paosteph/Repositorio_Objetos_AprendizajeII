from django.contrib import admin
from apps.gestorObjetos.models import Objeto, EspecificacionLOM, Repositorio, PalabraClave, Autor, RutaCategoria, UserProfile
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.sites.models import Site

"""
Clase que permite sobre escribir la clase usuario del sistema de autenticación de Django para inclui más campos
"""
class UserProfileInline(admin.StackedInline):
	model = UserProfile

"""
habilita la vista del perfil del usuario desde la interfaz de administración
"""
class UserProfileAdmin(UserAdmin):
	inlines = [UserProfileInline]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Objeto)
admin.site.register(EspecificacionLOM)
admin.site.register(Repositorio)
admin.site.register(PalabraClave)
admin.site.register(Autor)
admin.site.register(RutaCategoria)
admin.site.unregister(Site)