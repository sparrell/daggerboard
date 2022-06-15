from django import forms
from django.forms import ModelForm
from .models import Sbom,Package,SbomUpload
    
class vendorPickerform(ModelForm):
    """
    Form to populate vendor data on the vendor scorecard.
    """
    class Meta:
        model = Sbom
        fields = ['id', ]


class SbomForm(forms.ModelForm):
    """
    Form used for uploading SBOMs for analysis.
    """
    class Meta:
        model = SbomUpload
        fields=('sbomfile'),
        widgets = {'sbomfile': forms.ClearableFileInput(attrs={'multiple': True}),}


