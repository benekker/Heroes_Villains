from django.db import models

class Super(models.model):
    name = models.CharField(max_length=100)
    alter_ego = models.CharField(max_length=100)
    primary_ability = models.CharField(max_length=150)
    secondary_ability = models.CharField(max_length=150)
