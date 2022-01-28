import os
from django.db import models
from datetime import date

__all__ = ['Blacksmith']

class Blacksmith(models.Model):

        leather = models.CharField(max_length=255, blank=True, null=True)
        iron_ore = models.CharField(max_length=255, blank=True, null=True)
        animal_bone = models.CharField(max_length=255, blank=True, null=True)
        ebony = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return '%s' % (self.leather)