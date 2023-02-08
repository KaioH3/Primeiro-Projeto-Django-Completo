# from django.contrib import admin retirar isso porque só projeto precisa dessa linha
# adicionei este arquivo no app tasks para integrar o app ao projeto

from . import views # para importar, desta pasta(tasks), o views 

from django.urls import path

urlpatterns = [
    path('helloapp/', views.helloapp), # tem que falar que o app vem de views(views.app)
    path('', views.taskList, name='task-list'), # acessando o dominio do projeto(na barra, ou home(ou root(/)))
    path('task/<int:id>', views.taskView, name="task-view"),
    path('newtask/', views.newTask, name="new-task"),
    path('edit/<int:id>', views.editTask, name="edit-task"), # deve ter o id para que o user reveja a tarefa para editar-la melhor
    path('delete/<int:id>', views.deleteTask, name="delete-task"),
    path('yourname/<str:name>', views.yourName, name='your-name'), # poderia ser um inteiro ou outros tipos de dados 
    path('about-author', views.aboutAuthor, name='about-author'),
]                                               
# name é o apelido para esta view
# e em views do app eu crio a view                                                