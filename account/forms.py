from django import forms
from .models import *


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']
        #fields = '__all__'


class LoaderForm(forms.ModelForm):
    class Meta:
        model = Loader
        fields = '__all__'

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()