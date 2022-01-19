from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy

from main.models import Task


class LoginPage(LoginView):
    fields = '__all__'
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('tasks-list')


class RegisterPage(FormView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks-list')
        return super(RegisterPage, self).get(*args, **kwargs)


class TasksList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'main/tasks-list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False)
        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'completed']
    success_url = reverse_lazy('tasks-list')
    template_name = 'main/task-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'completed']
    success_url = reverse_lazy('tasks-list')
    template_name = 'main/task-form.html'


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks-list')
    template_name = 'main/task-delete.html'
