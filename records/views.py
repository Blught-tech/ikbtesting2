from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm  # Imports new form
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404
from django.contrib.admin.models import CHANGE # Import CHANGE for the audit log
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

@login_required
def user_profile(request):
    # 1. Logic for Profile
    task_count = Task.objects.filter(owner=request.user).count()
    completed_tasks = Task.objects.filter(owner=request.user, is_completed=True).count()

    context = {
        'user': request.user,
        'task_count': task_count,
        'completed_tasks': completed_tasks,
    }
    # 2. Return the profile template
    return render(request, 'records/profile.html', context)

@login_required
def task_list(request):
    # 1. Logic for Task List
    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
    # 2. Return the task list template
    return render(request, 'records/task_list.html', {'tasks': tasks})

@login_required
def toggle_task(request, task_id):
    # Security: get_object_or_404 ensures the task exists AND belongs to the user
    task = get_object_or_404(Task, id=task_id, owner=request.user)
    
    # Toggle the status
    task.is_completed = not task.is_completed
    task.save()

    # Manual Audit Log Entry for the update
    LogEntry.objects.create(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(Task).pk,
        object_id=str(task.pk),
        object_repr=force_str(task.title),
        action_flag=CHANGE,
        change_message=f"Status toggled to {'Completed' if task.is_completed else 'Pending'}"
    )

    return redirect('task_list')


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()

            # The newer, more compatible way to write to the Audit Log
            LogEntry.objects.create(
                user_id=request.user.id,
                content_type_id=ContentType.objects.get_for_model(Task).pk,
                object_id=str(task.pk),
                object_repr=force_str(task.title)[:200],
                action_flag=ADDITION,
                change_message="Task created via user form"
            )
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'records/task_form.html', {'form': form})



def home(request):
    return render(request, 'records/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('home') # Redirect to Home page
    else:
        form = UserCreationForm()
    return render(request, 'records/register.html', {'form': form})
