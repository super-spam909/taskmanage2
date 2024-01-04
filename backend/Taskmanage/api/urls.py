from django.urls import path 
from .views import UserViews


urlpatterns=[
    path("showUsers/", UserViews.getUsers),
    path("registerUser/", UserViews.registerUser),

    
]