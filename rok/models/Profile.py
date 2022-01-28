import os
from django.db import models
from datetime import date

__all__ = ['Profile']

class Profile(models.Model):

        governor_name = models.CharField(max_length=255, blank=True, null=True)
        governor_id = models.CharField(max_length=255, blank=True, null=True)
        power = models.CharField(max_length=255, blank=True, null=True)
        kill_points = models.CharField(max_length=255, blank=True, null=True)
        civilization = models.CharField(max_length=255, blank=True, null=True)
        kingdom = models.CharField(max_length=255, blank=True, null=True)
        alliance = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return '%s' % (self.governor_name)