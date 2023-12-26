from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class MyModelName(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """

    # Campos
    my_field_name = models.CharField(max_length=20, help_text="Enter field documentation")
    ...

    # Metadata
    class Meta:
        ordering = ["-my_field_name"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto MyModelName (en el sitio de Admin, etc.)
        """
        return self.field_name

class Curso(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100,default="")
    description = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):

        return reverse('curso-detail', args=[str(self.id)])

    
class Tarea(models.Model):
    titulo = models.CharField(max_length=200,default="")
    descripcion = models.CharField(max_length=500, null=True)

    curso = models.ForeignKey('Curso', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.curso}  --  {self.titulo}"
    
    def get_absolute_url(self):

        return reverse('tarea-detail', args=[str(self.id)])
    
class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    firstName = models.CharField(max_length=100,default="")
    lastName = models.CharField(max_length=100,default="")
    direccion = models.CharField(max_length=100, default="")
    birthdate = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.firstName
    def get_student_absolute_url(self):

        return reverse('estudiante-detail', args=[str(self.id)])
    
class Nota(models.Model):
    id = models.AutoField
    tarea = models.ForeignKey('Tarea' , on_delete=models.SET_NULL, null= True)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey('Curso', on_delete=models.SET_NULL, null=True)
    nota = models.FloatField(default=0.0,max_length=10)
    def __str__(self):
        return f"{self.estudiante}  --  {self.tarea}  --  Nota: {self.nota}"
    def get_absolute_url(self):

        return reverse('nota-detail', args=[str(self.id)])
    
class EntregaTarea(models.Model):
    id = models.AutoField
    tarea = models.ForeignKey('Tarea', on_delete=models.SET_NULL, null=True)
    estudiante = models.ForeignKey('Estudiante', on_delete=models.SET_NULL, null=True)
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    archivo = models.FileField(upload_to='entregas/', null=True)
    Comentarios = models.CharField(max_length=100,default="",blank=True)
    def __str__(self):
        fecha_hora_formateada = self.fechaEntrega.strftime("%Y-%m-%d %H:%M:%S")
        return f"{self.tarea} -- {self.estudiante}  -- {fecha_hora_formateada}"
    
    
