from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def viewCategory(request):
    category = Category.objects.all()
    if (request.method == "POST"):
        categoryform = CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('viewCategory')
    categoryform = CategoryForm()
    view_data = {
        "category": category,
        'form': categoryform
    }
    return render(request, 'viewCategory.html',view_data)

def viewTask(request, id):
    if request.method == "POST":
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid():
            taskForm.save()
            return redirect('viewTask', id)
    completed_task = Task.objects.filter(owner=id, status=True)
    pending_task = Task.objects.filter(owner=id, status=False)
    view_data = {
        "completed": completed_task,
        "pending": pending_task,
        "form": TaskForm(),
        "id": id
    }

    return render(request, 'viewItems.html', view_data)

def updateCategory(request, id):
    updating_data = Category.objects.get(id=id)
    categoryform = CategoryForm(instance=updating_data)
    if (request.method == "POST"):
        categoryform = CategoryForm(request.POST, instance=updating_data)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('viewCategory')
    return render(request, 'viewCategory.html', {'forms': categoryform, 'id': id})

def updateTask(request, id):
    updating_data = Task.objects.get(id=id)
    Task.objects.filter(id=id).update(status=not (updating_data.status))
    return redirect('viewCategory')
def editTask(request,id):
    if request.method == "POST":
        updating_data = TaskForm.objects.get(id=id)

        form=TaskForm(request.POST or None, instance=taskForm)
        if TaskForm.is_valid():
            TaskForm.save()

            massages.success(request,('Task Has Been Added'))
            return redirect('editTask', id)

    view_data = {

        "form": TaskForm,
        "id": id
    }
    return render(request,'editItems.html',view_data)