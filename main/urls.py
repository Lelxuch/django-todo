from django.urls import path
from django.contrib.auth.views import LogoutView

from main.views import TasksList, TaskCreate, TaskUpdate, TaskDelete, LoginPage, RegisterPage

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', TasksList.as_view(), name='tasks-list'),
    path('add-task/', TaskCreate.as_view(), name='add-task'),
    path('edit-task/<int:pk>', TaskUpdate.as_view(), name='edit-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
]
