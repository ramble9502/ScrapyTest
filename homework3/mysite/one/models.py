from __future__ import unicode_literals

from django.db import models

# Create your models here.


class kormovie(models.Model):
    title = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    img = models.ImageField()

    def __unicode__(self):
        return self.title
