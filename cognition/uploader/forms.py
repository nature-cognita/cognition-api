from django import forms

from .models import DataFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = DataFile
        fields = ["file"]
