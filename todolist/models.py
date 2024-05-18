from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=45)
    desc = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    due_time = models.TimeField()
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'