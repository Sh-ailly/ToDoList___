from django.db import models

# Create your models here.
class todomodel(models.Model):

    title=models.CharField(max_length=100)
    description=models.TextField()
    completed=models.BooleanField(default=False)

