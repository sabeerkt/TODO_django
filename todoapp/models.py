from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=250)
    priority = models.IntegerField()
    due_date = models.DateField()

# other models, if any
