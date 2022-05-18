from django import forms
from nft.models import ImageNFT


class GenerateNFTForm(forms.ModelForm):
    class Meta:
        model = ImageNFT
        fields = ["user"]
