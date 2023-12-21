# urls.py
from turtle import update
from django.urls import path
from .views import TaskDetailView, TaskListveiw, add, details, dlt, update_task

urlpatterns = [
    path('', add, name='add'),  # Assuming 'add' is your main view
    path('details/', details, name='details'),
    path('dlt/<int:taskid>/', dlt, name='dlt'),
    path('update/<int:id>/', update_task, name='update'),
    path("clshome/",TaskListveiw.as_view(),name="clshome"),
    path("dethome/", TaskDetailView.as_view(), name="dethome")


    # Add other URLs as needed
]
