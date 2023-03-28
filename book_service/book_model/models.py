from __future__ import unicode_literals
from django.db import models


# This is our model for user registration.
class book_details(models.Model):
    ### The following are the fields of our table.
    book_id = models.CharField(max_length=10)
    author=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    book_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=15)
    price = models.CharField(max_length=10)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s %s %s' % (self.book_id, self.author, self.description,
                                   self.book_name, self.availability, self.price)
