from django.db import models

# item model


class Item(models.Model):

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=500)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item_name
