from django.db import models
# from datetime import date


# Create your models here.

class Todo(models.Model):
    title=models.CharField(max_length=120)
    description=models.CharField(max_length=500)
    assignTo=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
    # date=models.DateField(default=date.today)
    

    def __str__(self):
        return self.title
