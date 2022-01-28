import os
from django.db import models
from datetime import date

__all__ = ['Boost']

class Boost(models.Model):

        EXPANDED_TRAINING = (
            ('lvl 1', 'Lvl 1'),
            ('lvl 2', 'Lvl 2'),
            ('lvl 3', 'Lvl 3'),
            ('lvl 4', 'Lvl 4'),
            ('lvl 5', 'Lvl 5'),
            ('lvl 6', 'Lvl 6'),
        )

        PEACE_SHIELD = (
            ('8 hours', '8 Hours'),
            ('24 hours', '24 Hours'),
        )

        ENHANCED_GATHERING = (
            ('8 hours', '8 Hours'),
            ('24 hours', '24 Hours'),
        )

        ENHANCED_ATTACK = (
            ('12 hours', '12 Hours'),
            ('24 hours', '24 Hours'),
        )

        ENHANCED_DEFENSE = (
            ('12 hours', '12 Hours'),
            ('24 hours', '24 Hours'),
        )

        ARMY_EXPANSION = (
            ('25%', '25%'),
            ('50%', '50%'),
        )

        FOOD_BOOST = (
            ('8 hours', '8 Hours'),
            ('24 hours', '24 Hours'),
        )

        WOOD_BOOST = (
            ('8 hours', '8 Hours'),
            ('24 hours', '24 Hours'),
        )

        STONE_BOOST = (
            ('8 hours', '8 Hours'),
            ('24 hours', '24 Hours'),
        )

        GOLD_BOOST = (
            ('8 hours', '8 Hours'),
            ('24 hours', '24 Hours'),
        )

        expanded_training = models.CharField(choices=EXPANDED_TRAINING, max_length=30, null=True)
        peace_shield = models.CharField(choices=PEACE_SHIELD, max_length=30, null=True)
        enhanced_gathering = models.CharField(choices=ENHANCED_GATHERING, max_length=30, null=True)
        enhanced_attack = models.CharField(choices=ENHANCED_ATTACK, max_length=30, null=True)
        enhanced_defense = models.CharField(choices=ENHANCED_DEFENSE, max_length=30, null=True)
        anti_reconnaissance_technology = models.CharField(max_length=255, blank=True, null=True)
        deceptive_troops = models.CharField(max_length=255, blank=True, null=True)
        army_expansion = models.CharField(choices=ARMY_EXPANSION, max_length=30, null=True)
        food_boost = models.CharField(choices=FOOD_BOOST, max_length=30, null=True)
        wood_boost = models.CharField(choices=WOOD_BOOST, max_length=30, null=True)
        stone_boost = models.CharField(choices=STONE_BOOST, max_length=30, null=True)
        gold_boost = models.CharField(choices=GOLD_BOOST, max_length=30, null=True)

        def __str__(self):
            return '%s' % (self.expanded_training)