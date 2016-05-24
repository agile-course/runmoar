from __future__ import unicode_literals

from django.db import models


class DateStatus(models.Model):

    class Meta:
        ordering = ('date', )

    date = models.DateField(unique=True)
    completed = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0.date} {0.completed}'.format(self)
