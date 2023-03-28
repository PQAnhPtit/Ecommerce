from __future__ import unicode_literals
from django.db import models


# This is our model for user registration.
class cart_details(models.Model):
    ### The following are the fields of our table.
    user_id = models.CharField(max_length=10)
    product_id = models.CharField(max_length=10)
    amount = models.CharField(max_length=10)
    price = models.CharField(max_length=10)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s' % (self.user_id, self.product_id,
                                   self.amount, self.price)
