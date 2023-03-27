from __future__ import unicode_literals
from django.db import models


# This is our model for user registration.
class order_details(models.Model):
    ### The following are the fields of our table.
    user_id = models.CharField(max_length=10)
    cart_id = models.CharField(max_length=10)
    created_date = models.CharField(max_length=100)
    total_price = models.CharField(max_length=10)

    ### It will help to print the values.
    def __str__(self):
        return '%s %s %s %s' % (self.user_id, self.cart_id,
                                   self.created_date, self.total_price)

