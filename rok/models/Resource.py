import os
from django.db import models
from datetime import date

__all__ = ['Resource']

class Resource(models.Model):

        food = models.CharField(max_length=255, blank=True, null=True)
        wood = models.CharField(max_length=255, blank=True, null=True)
        stone = models.CharField(max_length=255, blank=True, null=True)
        gold = models.CharField(max_length=255, blank=True, null=True)
        gems = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return '%s' % (self.food)