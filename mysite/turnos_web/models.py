from django.db import models


class Concept(models.Model):
    name = models.CharField(max_length=200)
