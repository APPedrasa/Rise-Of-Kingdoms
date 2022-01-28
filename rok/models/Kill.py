import os
from django.db import models
from datetime import date

__all__ = ['Kill']

class Kill(models.Model):

        tier_1 = models.CharField(max_length=255, blank=True, null=True)
        tier_2 = models.CharField(max_length=255, blank=True, null=True)
        tier_3 = models.CharField(max_length=255, blank=True, null=True)
        tier_4 = models.CharField(max_length=255, blank=True, null=True)
        tier_5 = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return '%s' % (self.tier_1)