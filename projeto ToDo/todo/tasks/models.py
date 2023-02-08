from django.db import models

from django.contrib.auth import get_user_model # metodo para o id unico do ForeignKey

# Create your models here.

class Task(models.Model): # herda as propiedades de models.Model
    
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    # daqui que vem o {{task.title}} do list.html
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField( # para saber se a tarefa está pronta
        max_length=5,
        choices=STATUS,
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) # criando o campo do id unico do usuario que está logado; "on_delete=models.CASCADE" serve para que quando o user for apagado todas as tarefas dele sejam apagadas também. Isto não é bom para sistemas em que é necessario guardar alguns registros antigospython manage.py makemigrations
    # agora como o campo user foi adicionado recentemente, é necessario fazer uma migração, parando o servidor e escrevendo "python3 manage.py makemigrations" na pasta "todo"; aparecerá um erro, pois tem tarefas que não tem usuario(ou dono) definido, então se faz necessario popular o banco de dados com estas informações, eu escolhi a opção 1, aonde vai atribuir todas as tarefas para o usuario de escolha, que nesse caso foi o 1(admin)
    # e depois faço o migrate com "python3 manage.py migrate"
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add: registra dia, mes e ano, e horario, automaticamente quando o registro é criado
    update_at = models.DateTimeField(auto_now=True) #registra sempre que é atualizado

    def __str__(self): # muda o nome da tarefa de Task object para o título da tarefa
        return self.title
