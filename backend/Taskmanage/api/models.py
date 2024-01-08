from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=15)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    