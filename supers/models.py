from django.db import models

from super_types.models import SuperType

class Super(models.Model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=150)
    secondary_ability = models.CharField(max_length=150)
    catchphrase = models.CharField(max_length=200)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)

class Power(models.Model):
    name = models.CharField(max_length=100)
