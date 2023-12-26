from django.shortcuts import render
from .models import Curso,Estudiante,Tarea,EntregaTarea,Nota
from django.views import generic
from django.contrib.auth.decorators import login_required

def index(request):
    num_alum=Estudiante.objects.all().count()
    num_tareas=Tarea.objects.all().count()
    num_cursos= Curso.objects.all().count()
    
    return render(
        request,
        'index.html',
        context=
        {'num_alum':num_alum,'num_tareas':num_tareas,'num_cursos':num_cursos},
    )
class TareasListView(generic.ListView):
    model = Tarea
    
class TareasDetailView(generic.DetailView):
    model = Tarea
    paginate_by = 10
    
    
    
class StudentsListView(generic.ListView):
    model = Estudiante
    
class StudentsDetailView(generic.DetailView):
    model = Estudiante
    paginate_by = 10
    
    
class CoursesListView(generic.ListView):
    model = Curso
    
class CoursesDetailView(generic.DetailView):
    model = Curso
    paginate_by = 10
    
    
class NotasListView(generic.ListView):
    model = Nota
    
    


@login_required
def notas_estudiante(request):
    estudiante = request.user.estudiante
    notas = Nota.objects.filter(estudiante=estudiante)
    return render(request, 'StudentsTasks/nota_list.html', {'notas': notas})
