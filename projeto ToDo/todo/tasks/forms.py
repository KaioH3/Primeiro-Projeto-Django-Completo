from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task # aqui eu defino o model que eu importei lá emcima
        fields = ('title', 'description') # campos que devem aparecer no frontend
        # o titulo e a descrição da tarefa são necessários por isso aparecem acima, diferente do campo "done", 
        # já que o padrão é aparecer como "Doing"(fazendo), quando a tarefa é criada
        # e o campo "id" o próprio django já fornece