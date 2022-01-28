import os
from django.db import models
from datetime import date

__all__ = ['Speedup']

class Speedup(models.Model):

        BUILDING = (
            ('1 minute', '1 Minute'),
            ('5 minutes', '5 Minutes'),
            ('10 minutes', '10 Minutes'),
            ('15 minutes', '15 Minutes'),
            ('30 minutes', '30 Minutes'),
            ('60 minutes', '60 Minutes'),
            ('3 hours', '3 Hours'),
            ('8 hours', '8 Hours'),
            ('15 hours', '15 Hours'),
            ('24 hours', '24 Hours'),
        )

        TRAINING = (
            ('1 minute', '1 Minute'),
            ('5 minutes', '5 Minutes'),
            ('10 minutes', '10 Minutes'),
            ('15 minutes', '15 Minutes'),
            ('30 minutes', '30 Minutes'),
            ('60 minutes', '60 Minutes'),
            ('3 hours', '3 Hours'),
            ('8 hours', '8 Hours'),
            ('15 hours', '15 Hours'),
            ('24 hours', '24 Hours'),
        )

        RESEARCH = (
            ('1 minute', '1 Minute'),
            ('5 minutes', '5 Minutes'),
            ('10 minutes', '10 Minutes'),
            ('15 minutes', '15 Minutes'),
            ('30 minutes', '30 Minutes'),
            ('60 minutes', '60 Minutes'),
            ('3 hours', '3 Hours'),
            ('8 hours', '8 Hours'),
            ('15 hours', '15 Hours'),
            ('24 hours', '24 Hours'),
        )

        HEALING = (
            ('1 minute', '1 Minute'),
            ('5 minutes', '5 Minutes'),
            ('10 minutes', '10 Minutes'),
            ('15 minutes', '15 Minutes'),
            ('30 minutes', '30 Minutes'),
            ('60 minutes', '60 Minutes'),
            ('3 hours', '3 Hours'),
            ('8 hours', '8 Hours'),
            ('15 hours', '15 Hours'),
            ('24 hours', '24 Hours'),
        )

        UNIVERSAL = (
            ('1 minute', '1 Minute'),
            ('5 minutes', '5 Minutes'),
            ('10 minutes', '10 Minutes'),
            ('15 minutes', '15 Minutes'),
            ('30 minutes', '30 Minutes'),
            ('60 minutes', '60 Minutes'),
            ('3 hours', '3 Hours'),
            ('8 hours', '8 Hours'),
            ('15 hours', '15 Hours'),
            ('24 hours', '24 Hours'),
        )

        building_speedup = models.CharField(choices=BUILDING, max_length=30, null=True)
        bquantity = models.CharField(max_length=255, blank=True, null=True)
        traing_speedup = models.CharField(choices=TRAINING, max_length=30, null=True)
        tquantity = models.CharField(max_length=255, blank=True, null=True)
        research_speedup = models.CharField(choices=RESEARCH, max_length=30, null=True)
        rquantity = models.CharField(max_length=255, blank=True, null=True)
        healing_speedup = models.CharField(choices=HEALING, max_length=30, null=True)
        hquantity = models.CharField(max_length=255, blank=True, null=True)
        universal_speedup = models.CharField(choices=UNIVERSAL, max_length=30, null=True)
        uquantity = models.CharField(max_length=255, blank=True, null=True)

        def __str__(self):
            return '%s' % (self.building_speedup)