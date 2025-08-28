from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Task

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

class TaskUpdateView(UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ["name","flag","description"]
    success_url = reverse_lazy('task-list')

class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    fields = ["name", "flag","description"]
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = "task/task_confirm_delete.html"
    success_url = reverse_lazy('task-list')