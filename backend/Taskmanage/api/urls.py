from django.urls import path 
from .views import UserViews, TaskViews


urlpatterns=[
    path("showUsers/", UserViews.getUsers),
    path("registerUser/", UserViews.registerUser ),
    path("login/", UserViews.login),
    path("logout/", UserViews.logout),
    path("whoamI/", UserViews.whoamI),
    path("CreateTask/", TaskViews.CreateTask),
    path("GetTasks/", TaskViews.GetTasks),
    path("DeleteTask/", TaskViews.DeleteTask),
    path("TaskDetail/", TaskViews.TaskDetail),
    path("UpdateTask/", TaskViews.UpdateTask),
    #path("resetPassword/", UserViews.resetPassword),

    

    
]