from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('tareas/', views.TareasListView.as_view(), name='tareas'),
    path('tarea/<int:pk>', views.TareasDetailView.as_view(), name='tarea-detail'),
    path('students/', views.StudentsListView.as_view(), name='students'),
    path('student/<int:pk>', views.StudentsDetailView.as_view(), name='estudiante-detail'),
    path('courses/', views.CoursesListView.as_view(), name='courses'),
    path('course/<int:pk>', views.CoursesDetailView.as_view(), name='curso-detail'),
    path('notas/', views.notas_estudiante, name='notas'),
    
]
