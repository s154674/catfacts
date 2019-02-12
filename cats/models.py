from django.db import models

# Create your models here.


class Catfact(models.Model):
    text = models.TextField()
    api_id = models.CharField(max_length=40)
