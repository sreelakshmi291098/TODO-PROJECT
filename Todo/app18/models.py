from django.db import models

# Create your models here.
class Todo(models.Model):
    Taskname=models.CharField(max_length=30)
    Priority=models.IntegerField(unique=True)
    Date=models.DateField()