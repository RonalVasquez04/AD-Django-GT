from django.contrib import admin
from .models import Curso,Estudiante,Tarea,EntregaTarea,Nota

# Register your models here.
admin.site.register(Curso)
#admin.site.register(Estudiante)
admin.site.register(Tarea)
admin.site.register(EntregaTarea)
admin.site.register(Nota)

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('firstName','lastName')
