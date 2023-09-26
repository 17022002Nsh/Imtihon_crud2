from django.shortcuts import render, redirect
from .models import Todo

def home(request):
    
    tasks = Todo.objects.all()
    
    context = {
        'tasks' : tasks
    }
    
    return render(request, 'index.html', context)



def create_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        
        todo = Todo(
            title=title
        )
        todo.save()
        return redirect("home")
    return render(request, 'create.html')

def edit_todo(request, pk):
    task = Todo.objects.get(id=pk)
    
    context = {
        'task':task
    }
    
    if request.method == "POST":
        vazifa = request.POST.get("title")
        task.title = vazifa
        
        task.save()
        return redirect('home')
    
    return render(request, 'edit.html', context)

def delete_todo(request, pk):
    vazifa = Todo.objects.get(id=pk)
    vazifa.delete()
    return redirect("home")
        
