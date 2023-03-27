from __future__ import unicode_literals
from django.db import models


# This is our model for user registration.
class comment_details(models.Model):
    ### The following are the fields of our table.
    user_id = models.CharField(max_length=10)
    description = models.CharField(max_length=10)
    created_date = models.CharField(max_length=100)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s' % (self.user_id, self.description, self.created_date)
