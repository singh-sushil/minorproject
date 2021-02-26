from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = [
            "owners_name",
            "Address",
            "contact_number",
            "location",
            "amount",
            "length",
            "Area",
            "image1",
            "image2",
            "image3",
            "image4",
            "payment_verification_slip",
        ]
