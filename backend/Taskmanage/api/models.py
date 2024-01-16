from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    