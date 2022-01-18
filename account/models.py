from django.db import models
import os


class Brand(models.Model):
    name = models.CharField(max_length=191, blank=True)
    image = models.ImageField(upload_to="images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
         return self.name

class Loader(models.Model):
     price = models.FileField(upload_to="files")
     executed = models.IntegerField(blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     #brand = models.ForeignKey('Loader', on_delete=models.PROTECT)
     brand_id = models.IntegerField(blank=True, null=True)
     user = models.CharField(max_length=191, blank=True)

     def filename(self):
          return os.path.basename(self.price.name)

     def __iter__(self):
          for field_name in self._meta.get_all_field_names():
               value = getattr(self, field_name, None)
               yield (field_name, value)



class Rule(models.Model):
     brand_id = models.IntegerField(null=True)
     loader_id = models.IntegerField(null=True)
     type = models.CharField(max_length=191, blank=True, null=True)  ####### brand, price, sheet
     sheet_id = models.IntegerField(null=True)
     #sheet = models.CharField(max_length=191, blank=True, null=True)
     sheets = models.CharField(max_length=191, blank=True, null=True)
     start_from =models.IntegerField(null=True)
     remove_charter_all =models.CharField(max_length=191, blank=True, null=True)
     remove_charter =models.CharField(max_length=191, blank=True, null=True)
     remove_charter_sku =models.CharField(max_length=191, blank=True, null=True)

     #
     r_what = models.TextField(blank=True)
     r_forwhat = models.TextField(blank=True)
     r_from_sku = models.TextField(blank=True)

     sku = models.CharField(max_length=191, blank=True, null=True)
     msrp = models.CharField(max_length=191, blank=True, null=True)
     map = models.CharField(max_length=191, blank=True, null=True)
     our_price = models.CharField(max_length=191, blank=True, null=True)
     field_not_empty = models.CharField(max_length=191, blank=True, null=True)
     rules = models.TextField(blank=True)
     ignore_skus = models.TextField(blank=True)
     checkbox = models.CharField(max_length=10, blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


class Replaced(models.Model):
     rule_id = models.IntegerField(null=True)
     what = models.CharField(max_length=191, blank=True, null=True)
     for_what = models.CharField(max_length=191, blank=True, null=True)
     field = models.CharField(max_length=191, blank=True, null=True)
     ignore_sku = models.CharField(max_length=191, blank=True, null=True)


class Matching(models.Model):
     rule_id = models.IntegerField(null=True)
     sku = models.CharField(max_length=191, blank=True, null=True)
     msrp = models.CharField(max_length=191, blank=True, null=True)
     map = models.CharField(max_length=191, blank=True, null=True)
     our_price = models.CharField(max_length=191, blank=True, null=True)
     brand = models.CharField(max_length=191, blank=True, null=True)
     field_not_empty = models.CharField(max_length=191, blank=True, null=True)
     rules = models.TextField(blank=True)



class Replace(models.Model):
     what = models.CharField(max_length=191, blank=True, null=True)
     forwhat = models.CharField(max_length=191, blank=True, null=True)

# Replace Charter
class Rcharter(models.Model):
     rule_id = models.IntegerField(null=True)
     what = models.CharField(max_length=191, blank=True, null=True)
     forwhat = models.CharField(max_length=191, blank=True, null=True)

# Replace SKU
class Rsku(models.Model):
     rule_id = models.IntegerField(null=True)
     what = models.CharField(max_length=191, blank=True, null=True)
     forwhat = models.CharField(max_length=191, blank=True, null=True)




#class Matching(models.Model):
#     file_id = models.IntegerField(null=True)
##     brand_id = models.IntegerField(null=True)
 ##    sheet = models.CharField(max_length=191, blank=True, null=True)
  #
     #db_index = models.IntegerField(null=True)
    # file_index = models.IntegerField(null=True)
    # field_not_empty = models.CharField(max_length=191, blank=True, null=True)
    # rules = models.TextField(blank=True)
    ## created_at = models.DateTimeField(auto_now_add=True)
     ##updated_at = models.DateTimeField(auto_now=True)