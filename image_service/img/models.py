from __future__ import unicode_literals
from django.db import models


# This is our model for user registration.
class img_details(models.Model):
    ### The following are the fields of our table.
    link = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    item = models.CharField(max_length=10)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s' % (self.link, self.description, self.item)
