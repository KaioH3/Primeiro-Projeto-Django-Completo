from django.shortcuts import render, get_object_or_404, redirect #(metodo get_object_or_404: get o objeto ou dá erro)

from django.contrib.auth.decorators import login_required # decorator necessario para bloquear as tarefas a usuarios não logadoss

from django.core.paginator import Paginator

from django.http import HttpResponse # importando a função HttpResponse

from .forms import TaskForm # importando o formulário de forms.py

from django.contrib import messages # para o sistema de confirmação de delete

from .models import Task

# Create your views here.
@login_required #com este decorator, a view só aparecerá ao usuario logado
def taskList(request):
    search = request.GET.get('search') #name do objeto html de input do forms

    if search:

        # tasks = Task.objects.filter(title__icontains=search) # o "i" de icontains ignora o Case sensitive
        tasks = Task.objects.filter(title__icontains=search, user=request.user) # faz a busca somente do usuario que está no request(user=request.user)
    else:

        #tasks_list = Task.objects.all().order_by('-created_at') # esta variavel contem todas as tasks
        # e mostrará-las ordenadas pelas(.order_by) tarefas mais novas(-created_at), sendo o menos(-) um alternador de ordem  

        tasks_list = Task.objects.all().order_by('-created_at').filter(user=request.user) # agora com o filtro de usuario autenticado
        paginator = Paginator(tasks_list, 3) # Mostra as tarefas da lista de tarefas de 3 em 3

        page = request.GET.get('page') # resgata o argumento do request, pegando a página atual na url

        tasks = paginator.get_page(page) # paginator com a pagina atual, que mostrará as 3 tasks 

    return render(request, 'tasks/list.html', {'tasks': tasks}) # no django, o padrão é de que os templates fiquem na pasta templates

@login_required
def taskView(request, id): # recebe request e o id da task
    task = get_object_or_404(Task, pk=id) # o metodo recebe dois argumentos: o model e o id(pk: primary key, referencia que ele vai buscar)
    return render(request, 'tasks/task.html', {'task': task}) # a função de cima retorna o template das tarefas(plural) renderizados e esta retorna o templete de cada tarefa 

@login_required
def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST) # se for 'POST', preenche o form com os dados

        if form.is_valid():
            task = form.save(commit=False) # o commit=False faz com que a função espere até que mande salvar a tarefa,
            # permitindo que qualquer modificação seja feita 
            task.done = 'doing' # muda o valor do campo "done" como "doing"
            task.user = request.user # usuario autenticado
            task.save() # e finalmente, salva a tarefa 
            return redirect('/') # E redireciona para o barra('/'), mais um shortcut(atalho) do django 

    else:    
        form = TaskForm()
        return render(request, 'tasks/addtask.html', {'form': form})

@login_required    
def editTask(request, id):
    task = get_object_or_404(Task, pk=id) # mesma coisa do addTask
    form = TaskForm(instance=task)

    if (request.method == 'POST'):
        form = TaskForm(request.POST, instance=task) # mesma coisa do newTask, sobrepondo a variavel de newTask

        if(form.is_valid()):
            task.save()
            return redirect('/')
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})     

    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})     

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso!') # uma mensagem que recebe um classe do tipo informação
    return redirect('/')

@login_required
# como coloquei o helloapp no do app tasks, preciso criar esta função request
def helloapp(request): 
    return HttpResponse('Hello World!')
 

def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})

def aboutAuthor(request):
    return render(request, 'about-author.html')