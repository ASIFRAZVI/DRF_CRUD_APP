from django.db import models

class crudobj(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
