from __future__ import unicode_literals
from django.db import models


# This is our model for user registration.
class cloth_details(models.Model):
    ### The following are the fields of our table.
    cloth_id = models.CharField(max_length=10)
    brand=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    cloth_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.cloth_id, self.brand, self.description,
                                   self.cloth_name, self.availability, self.price)
