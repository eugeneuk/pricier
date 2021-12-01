from django.db import models
'''
class PProduct(models.Model):
    name = models.CharField(max_length=191, blank=True, null=True, default=None)
    number = models.CharField(max_length=191, blank=True, null=True, default=None)
    category = models.CharField(max_length=191, blank=True, null=True, default=None)
    subcategory = models.CharField(max_length=191, blank=True, null=True, default=None)
    brand = models.CharField(max_length=191, blank=True, null=True, default=None)
    replacement = models.CharField(max_length=191, blank=True, null=True, default=None)
    aviable = models.IntegerField(null=True)
    price_changed = models.CharField(max_length=191, blank=True, null=True, default=None)
    upc = models.CharField(max_length=191, blank=True, null=True, default=None)
    upc_replace = models.CharField(max_length=191, blank=True, null=True, default=None)
    mpg = models.CharField(max_length=191, blank=True, null=True, default=None)
    hierarchy = models.CharField(max_length=191, blank=True, null=True, default=None)
    #price = models.IntegerField(null=True)
    price = models.CharField(max_length=191, blank=True, null=True, default=None)
    price_dealer = models.CharField(max_length=191, blank=True, null=True, default=None)
    price_dealer_max = models.IntegerField(null=True)
    description = models.TextField(blank=True, null=True, default=None)
    weight = models.CharField(max_length=191, blank=True, null=True, default=None)
    height = models.CharField(max_length=191, blank=True, null=True, default=None)
    width = models.CharField(max_length=191, blank=True, null=True, default=None)
    depth = models.CharField(max_length=191, blank=True, null=True, default=None)
    additional = models.TextField(blank=True, null=True, default=None)
    additional2 = models.TextField(blank=True, null=True, default=None)
    additional3 = models.TextField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
'''

class Product(models.Model):
        description = models.TextField(blank=True, null=True, default=None)
        sku = models.CharField(max_length=191, blank=True, null=True, default=None)
        msrp = models.CharField(max_length=191, blank=True, null=True, default=None)
        map = models.CharField(max_length=191, blank=True, null=True, default=None)
        our_price = models.CharField(max_length=191, blank=True, null=True, default=None)
        brand = models.CharField(max_length=191, blank=True, null=True, default=None)
        key = models.CharField(max_length=191, blank=True, null=True, default=None)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.description