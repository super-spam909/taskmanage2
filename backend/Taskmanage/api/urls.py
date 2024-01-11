from django.urls import path 
from .views import UserViews, TaskViews


urlpatterns=[
    path("showUsers/", UserViews.getUsers),
    path("register/", UserViews.registerUser, name="register"),
    path("login/", UserViews.login),
    path("CreateTask/", TaskViews.CreateTask),
    path("GetTasks/", TaskViews.GetTasks),
    path("DeleteTask/<int:pk>/", TaskViews.DeleteTask),
    path("TaskDetail/<int:pk>/", TaskViews.TaskDetail),
    path("UpdateTask/<int:pk>/", TaskViews.UpdateTask),
    #path("resetPassword/", UserViews.resetPassword),

    

    
]