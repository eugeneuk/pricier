from django import forms
from .models import *
from products.models import Product

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        #fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['sku', 'msrp', 'our_price', 'map']
        #fields = '__all__'

class LoaderForm(forms.ModelForm):
    class Meta:
        model = Loader
        fields = '__all__'

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class ReplacementForm(forms.Form):
    what = forms.CharField(initial=1, label='Replace SKU') #Replace SKU
    forwhat = forms.CharField(initial=2, label='By') #By
    file = forms.FileField()

