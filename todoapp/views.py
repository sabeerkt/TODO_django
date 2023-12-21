from django.shortcuts import redirect, render

from todoapp.forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
# to add function create function 
class TaskListveiw(ListView):
    model=Task
    template_name='index.html'
    #  which verible we we are fetched 
    context_object_name="fetch"
    
class TaskDetailView(DetailView):
    model=Task
    template_name='details.html'
    context_object_name="fetch"    
    
def add(request):
    fetch = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        due_date = request.POST.get('due_date', '')
        task = Task(name=name, priority=priority, due_date=due_date)
        task.save()
    return render(request, 'index.html', {"fetch": fetch})
def details(request):
    
    return render(request,"details.html")
def dlt(request,taskid):
    dlt=Task.objects.get(id=taskid)
    if request.method =="POST":
        dlt.delete()
        return redirect("/")
    return render(request,"dlt.html")


def  update_task(request, id):
    task = Task.objects.get(id=id)
    form = TodoForm(request.POST or None, instance=task)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "edit.html", {"form": form, "task": task})