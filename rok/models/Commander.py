import os
from django.db import models
from datetime import date

__all__ = ['Commander']

class Commander(models.Model):

        RARITY = (
            ('legendary', 'Legendary'),
            ('epic', 'Epic'),
            ('elite', 'Elite'),
            ('advanced', 'Advanced'),
        )
        
        CLASS = (
            ('infantry', 'Infantry'),
            ('cavalry', 'Cavalry'),
            ('archer', 'Archer'),
            ('mixed', 'Mixed'),
        )

        STAR_LEVEL = (
            ('one', 'One'),
            ('two', 'Two'),
            ('three', 'Three'),
            ('four', 'Four'),
            ('five', 'Five'),
            ('six', 'Six'),
        )

        SPECIALTY1 = (
            ('infantry', 'Infantry'),
            ('cavalry', 'Cavalry'),
            ('archer', 'Archer'),
            ('leadership', 'Leadership'),
            ('peacekeeping', 'PeaceKeeping'),
            ('versatility', 'Versatility'),
            ('integration', 'Integration'),
            ('garrison', 'Garrison'),
            ('conquering', 'Conquering'),
            ('skill', 'Skill'),
            ('attack', 'Attack'),
            ('defense', 'Defense'),
            ('mobility', 'Mobility'),
            ('support', 'Support'),
            ('gathering', 'Gathering'),
        )

        SPECIALTY2 = (
            ('infantry', 'Infantry'),
            ('cavalry', 'Cavalry'),
            ('archer', 'Archer'),
            ('leadership', 'Leadership'),
            ('peacekeeping', 'PeaceKeeping'),
            ('versatility', 'Versatility'),
            ('integration', 'Integration'),
            ('garrison', 'Garrison'),
            ('conquering', 'Conquering'),
            ('skill', 'Skill'),
            ('attack', 'Attack'),
            ('defense', 'Defense'),
            ('mobility', 'Mobility'),
            ('support', 'Support'),
            ('gathering', 'Gathering'),
        )

        SPECIALTY3 = (
            ('infantry', 'Infantry'),
            ('cavalry', 'Cavalry'),
            ('archer', 'Archer'),
            ('leadership', 'Leadership'),
            ('peacekeeping', 'PeaceKeeping'),
            ('versatility', 'Versatility'),
            ('integration', 'Integration'),
            ('garrison', 'Garrison'),
            ('conquering', 'Conquering'),
            ('skill', 'Skill'),
            ('attack', 'Attack'),
            ('defense', 'Defense'),
            ('mobility', 'Mobility'),
            ('support', 'Support'),
            ('gathering', 'Gathering'),
        )

        commander = models.CharField(max_length=255, blank=True, null=True)
        rarity = models.CharField(choices=RARITY, max_length=30, null=True)
        rokclass = models.CharField(choices=CLASS, max_length=30, null=True)
        star_level = models.CharField(choices=STAR_LEVEL, max_length=30, null=True)
        specialty1 = models.CharField(choices=SPECIALTY1, max_length=30, null=True)
        specialty2 = models.CharField(choices=SPECIALTY2, max_length=30, null=True)
        specialty3 = models.CharField(choices=SPECIALTY3, max_length=30, null=True)

        def __str__(self):
            return '%s' % (self.commander)