from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = [
            "Name",
            "Address",
            "phone_number",
            "url_location",
            "amount",
            "length",
            "breadth",
            "image1",
            "image2",
            "image3",
            "image4",
            "payment_method",
        ]
